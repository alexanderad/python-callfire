import base64
import sys
import json
import urllib
import urllib2
import logging

# set default logger handler
logging.getLogger(__name__).addHandler(logging.NullHandler())


class CallFireError(Exception):
    """Exception wrapper."""
    def __init__(self, wrapped_exc, *args, **kwargs):
        self.wrapped_exc = wrapped_exc
        super(CallFireError, self).__init__(*args, **kwargs)


class BaseResponse(object):
    """Response wrapper."""
    def __init__(self, response):
        self._response = response

    def __getattr__(self, item):
        if hasattr(self._response, item):
            return getattr(self._response, item)
        return getattr(self, item)

    def json(self):
        """Interprets the response as JSON."""
        return json.load(self._response)


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

    def _add_stderr_logger(self, level=logging.DEBUG):
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

    def _post(self, path, query=None, body=None):
        """Sends a single POST request.

        :param path: request path
        :param query: request query
        :param body: request body
        """
        return self._request(path, query, body, 'POST')

    def _get(self, path, query=None, body=None):
        """Sends a single GET request.

        :param path: request path
        :param query: request query
        :param body: request body
        """
        return self._request(path, query, body, 'GET')

    def _delete(self, path, query=None, body=None):
        """Sends a single DELETE request.

        :param path: request path
        :param query: request query
        :param body: request body
        """
        return self._request(path, query, body, 'DELETE')

    def _put(self, path, query=None, body=None):
        """Sends a single PUT request.

        :param path: request path
        :param query: request query
        :param body: request body
        """
        return self._request(path, query, body, 'PUT')

    def _request(self, path, query, body, method):
        """Sends a single API request.

        :param path: request path
        :param query: request query
        :param body: request body
        :param method: request method
        """
        query = query

        url = '{}{}'.format(self.BASE_URL, path)
        if query:
            url += '?{}'.format(urllib.urlencode(query))

        auth_header = base64.encodestring(
            '{}:{}'.format(self.username, self.password)).strip()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic {}'.format(auth_header),
        }

        data = None
        if body:
            data = json.dumps(body)

        request = urllib2.Request(url, data, headers)
        request.get_method = lambda: method

        try:
            return BaseResponse(urllib2.urlopen(request))
        except Exception as wrapped_exc:
            wrapped_exp_body = (
                wrapped_exc.fp.read() if wrapped_exc.fp else None)
            wrapped_exc_repr = '{}: {}'.format(wrapped_exc, wrapped_exp_body)

            self.logger.debug(
                "Error '%s' in context of method '%s %s' query '%s' body '%s' "
                "response body: '%s'",
                str(wrapped_exc), method, path, query, body, wrapped_exc_repr)

            exception_type, value, traceback = sys.exc_info()
            exception_wrapper = CallFireError(wrapped_exc, wrapped_exc_repr)
            raise CallFireError, exception_wrapper, traceback
