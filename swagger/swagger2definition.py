import json
import re
import urllib2


class Swagger2Definition(object):
    """Swagger to class definition adapter."""

    JSONRequest = 'JSONRequest'
    MultipartRequest = 'MultipartRequest'

    def __init__(self, schema):
        """Initialized generator.

        :param schema: schema
        """
        self.schema = schema

    def _camel_to_underscore(self, method_name):
        """Returns underscore version of camel case method.

        :param method_name: method name
        :returns underscore method name
        """
        return re.sub(r'([A-Z])+', r'_\1', method_name).lower()

    def _wrap_lines(self, long_line, n=79):
        """Wraps a string to be no longer than n characters.

        :param long_line: long line to wrap
        :param n: number of colons to wrap to
        :returns
        """
        words, lines = long_line.split(), []

        line = []
        while words:
            word = words.pop(0)
            if len(' '.join(line + [word])) <= n:
                line.append(word)
            else:
                lines.append(line)
                line = [word]
        else:
            lines.append(line)

        return map(lambda line: ' '.join(line), lines)

    def _get_method_args(self, params):
        """Returns path args declaration.

        :param params: params
        :return path args declaration.
        """
        return [p['name'] for p in params if p['in'] == 'path']

    def _get_method_kwargs(self, params, default=None):
        """Returns path kwargs declaration.

        :param params: params
        :return path kwargs declaration.
        """
        has_query_params = any([p for p in params if p['in'] == 'query'])
        has_body_params = any([p for p in params if p['in'] == 'body'])

        declarations = []
        if has_query_params:
            value = default
            if default == 'self':
                value = 'query'
            declarations.append('query={}'.format(value))

        if has_body_params:
            value = default
            if default == 'self':
                value = 'body'
            declarations.append('body={}'.format(value))

        return declarations

    def _get_param(self, param):
        """Generates single param declaration.

        :param param: param
        :returns param declaration
        """
        param.setdefault('type', '')
        return ':{in} {type} {name}: {description}'.format(**param)

    def _get_ref(self, ref_definition):
        """Gets reference name by definition.

        :param ref_definition: reference definition
        :returns reference
        """
        return ref_definition.split('/')[-1]

    def _get_by_ref(self, ref):
        """Gets leaf by reference.

        :param ref: reference
        :returns referenced leaf
        """
        return self.schema['definitions'].get(ref)

    def _get_body_params(self, param):
        """Parses body params into definitions.

        :param param: param
        :returns body params definitions
        """
        schema, params, ref = param['schema'], None, None

        if '$ref' in schema:
            ref = self._get_ref(schema['$ref'])
            params = self._get_by_ref(ref)
        elif 'items' in schema:
            ref = self._get_ref(schema['items']['$ref'])
            params = self._get_by_ref(ref)

        if not params:
            return []

        for name, property in params['properties'].items():
            property.update({'in': 'body -> {}'.format(ref), 'name': name})

        return self._get_params(params['properties'].values())

    def _get_params(self, params):
        """Generates params declarations.

        :param params: params
        :returns params declaration
        """
        declarations = []
        for param in params:
            param.setdefault('type', '')
            if param['in'] == 'body':
                declarations.append(self._get_param(param))
                declarations.extend(self._get_body_params(param))
                continue

            declarations.append(self._get_param(param))

        return declarations

    def _get_path_args(self, path, params):
        """Returns path format definition.

        :param path: path
        :param params: params
        :returns path definition
        """
        path_args = self._get_method_args(params)
        if not path_args:
            return "'{path}'".format(path=path)

        format_args = ', '.join(['{0}={0}'.format(arg) for arg in path_args])
        return "'{path}'.format({format_args})".format(
            path=path, format_args=format_args)

    def _add_line(self, line, level):
        """Add a single line.

        :param line: line
        :param level: indentation level
        """
        return '{}{}'.format(' ' * level * 4, line)

    def _generate_method(self, http_path, http_method, schema):
        """Generates method code for the leaf.

        :param http_path: http path
        :param http_method: http method
        :param schema: method leaf in object tree
        """
        lines = []

        consumes = schema['consumes'][0]
        consumes_requests = {
            'application/json': self.JSONRequest,
            'multipart/form-data': self.MultipartRequest,
        }
        request_type = consumes_requests[consumes]

        # header
        method_name = self._camel_to_underscore(schema['operationId'])
        method_args = ['self']
        method_args.extend(self._get_method_args(schema['parameters']))
        method_args.extend(self._get_method_kwargs(schema['parameters']))
        if request_type == self.MultipartRequest:
            # The multipart payload is not defined as a parameter in the
            # specification, just add it here.
            method_args.append('payload=None')

        lines.append('def {method_name}({args_and_kwargs}):'.format(
            method_name=method_name, args_and_kwargs=', '.join(method_args)))

        # docstring
        lines.append(self._add_line('"""{}.'.format(schema['summary']), 1))
        lines.append(self._add_line('', 1))
        wrapped_desc = self._wrap_lines(schema['description'], 79 - 4 * 2)
        lines.extend(map(lambda line: self._add_line(line, 1), wrapped_desc))
        lines.append(self._add_line('', 1))

        # params
        for line in self._get_params(schema['parameters']):
            for wrapped_line in self._wrap_lines(line, 79 - 4 * 2):
                lines.append(self._add_line(wrapped_line, 1))
        lines.append(self._add_line('"""', 1))

        # body
        method_args_and_kwargs = [
            self._get_path_args(http_path, schema['parameters'])]
        method_args_and_kwargs.extend(self._get_method_kwargs(
            schema['parameters'], 'self'))

        if request_type == self.MultipartRequest:
            method_args_and_kwargs.append('payload=payload')

        body = (
            "return self._{http_method}({request_type}({method_kwargs}))"
        ).format(
            http_method=http_method, http_path=http_path,
            method_kwargs=', '.join(method_args_and_kwargs),
            request_type=request_type,
        )
        lines.append(self._add_line(body, 1))
        lines.append(self._add_line('', 1))

        return '\n'.join(lines)

    def generate_code(self):
        """Generates code for a given schema.

        Prints generated code to stdout.
        """
        paths = sorted(data['paths'].keys())
        for path in paths:
            methods = sorted(data['paths'][path].keys())
            for method in methods:
                definition = data['paths'][path][method]
                print(self._generate_method(path, method, definition))


if __name__ == '__main__':
    SWAGGER_JSON = 'https://www.callfire.com/v2/api-docs/swagger.json'
    data = json.load(urllib2.urlopen(SWAGGER_JSON))
    Swagger2Definition(data).generate_code()
