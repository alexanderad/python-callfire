import abc
import base64
import json
import logging
import sys
import types
import six
try:
    # py3
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from urllib.error import URLError
except ImportError:
    # py2
    from urllib import urlencode
    from urllib2 import urlopen, Request, URLError


# set default logger handler
logging.getLogger(__name__).addHandler(logging.NullHandler())


class CallFireError(Exception):
    """Exception wrapper."""
    def __init__(self, wrapped_exc, *args, **kwargs):
        self.wrapped_exc = wrapped_exc
        super(CallFireError, self).__init__(*args, **kwargs)


@six.add_metaclass(abc.ABCMeta)
class BaseRequest(object):
    """Class for preparing a customized request."""

    def __init__(self, path, query=None, body=None, **kwargs):
        self.path = path
        self.query = query
        self.body = body

    @property
    @abc.abstractmethod
    def additional_headers(self):
        """Get a dictionary with additional headers for this request."""

    @property
    @abc.abstractmethod
    def prepared_body(self):
        """The prepared body

        This method should do everything necessary in ordr for the
        underlying body to be useful with this kind of request.
        """

    def prepare(self, base_url, auth_header, method):
        """Prepare the underlying request

        The act of preparation involves transforming the body
        into the right format, setting the required headers.

        :param method: The method with which this request is going to be used
        :returns: An instance of urllib.Request.
        """

        url = '{}{}'.format(base_url, self.path)
        if self.query:
            url += '?{}'.format(urlencode(self.query))

        headers = {'Authorization': auth_header}
        headers.update(self.additional_headers)

        request = Request(url, self.prepared_body, headers)
        request.get_method = lambda: method
        return request


class JSONRequest(BaseRequest):
    """A request which knows how to process JSON payloads."""

    additional_headers = {'Content-Type': 'application/json'}

    @property
    def prepared_body(self):
        if self.body:
            return json.dumps(self.body).encode('utf-8')


class MultipartRequest(BaseRequest):
    """Request which can be used for multipart form posting."""

    def __init__(self, *args, **kwargs):
        super(MultipartRequest, self).__init__(*args, **kwargs)
        self._payload = kwargs.pop('payload', None)
        self._prepared_body = None

    @property
    def additional_headers(self):
        return {
            'Content-type': 'multipart/form-data; boundary=boundary',
            'Content-Length': len(self.prepared_body),
        }

    @staticmethod
    def generate_multipart(file_stream):
        boundary = b'boundary'
        part_boundary = b'--' + boundary

        parts = [
            part_boundary,
            b'Content-Disposition: form-data; name="file"; filename="file"'
            b'\r\n',
            file_stream.read(),
            b'--' + boundary + b'--',
            b'',
        ]
        return b'\r\n'.join(parts)

    @property
    def prepared_body(self):
        if self._prepared_body:
            return self._prepared_body

        self._prepared_body = self.generate_multipart(self._payload)
        return self._prepared_body


class BaseAPI(object):
    #: Base API url
    BASE_URL = None
    #: Logger
    logger = logging.getLogger(__name__)

    def __init__(self, username, password, debug=False):
        """API base.

        :param username: API username
        :param password: API password
        :param debug: enable debug logger
        """
        self.username = username
        self.password = password
        if debug:
            self._add_stderr_logger()

    @staticmethod
    def _add_stderr_logger(level=logging.DEBUG):
        """Adds stderr logger for debug output.

        :param level: set logger level
        """
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)s %(message)s'))

        logger = logging.getLogger(__name__)
        logger.addHandler(handler)
        logger.setLevel(level)
        logger.debug('Enabled stderr debug logging at %s', __name__)

    def _post(self, request):
        """Sends a single POST request.

        :param request: The request object to be used.
        """
        return self._open_request(request, 'POST')

    def _get(self, request):
        """Sends a single GET request.

        :param request: The request object to be used.
        """
        return self._open_request(request, 'GET')

    def _delete(self, request):
        """Sends a single DELETE request.

        :param request: The request object to be used.
        """
        return self._open_request(request, 'DELETE')

    def _put(self, request):
        """Sends a single PUT request.

        :param request: The request object to be used.
        """
        return self._open_request(request, 'PUT')

    def _get_auth_header(self):
        """Returns authorization header value.

        :returns auth header
        """
        return 'Basic {}'.format(base64.b64encode(
            '{}:{}'.format(self.username, self.password).encode()
        ).strip().decode())

    def _open_request(self, request, method):
        """Sends a single API request.

        :param path: request path
        :param query: request query
        :param body: request body
        :param method: request method
        """
        prepared = request.prepare(
            base_url=self.BASE_URL,
            auth_header=self._get_auth_header(),
            method=method)
        try:
            response = urlopen(prepared)
            response.json = types.MethodType(
                lambda r: json.loads(r.read().decode('utf-8')), response)
            return response
        except URLError as wrapped_exc:
            wrapped_exp_body = 'None'
            if hasattr(wrapped_exc, 'fp') and wrapped_exc.fp:
                wrapped_exp_body = wrapped_exc.fp.read()

            wrapped_exc_repr = '{}: {}'.format(wrapped_exc, wrapped_exp_body)

            self.logger.debug(
                "Error '%s' in context of method '%s %s' query '%s' body '%s' "
                "response body: '%s'",
                repr(wrapped_exc), method, request.path,
                request.query, request.body, wrapped_exc_repr)

            _, _, traceback = sys.exc_info()
            exception_wrapper = CallFireError(wrapped_exc, wrapped_exc_repr)

            six.reraise(CallFireError, exception_wrapper, traceback)
