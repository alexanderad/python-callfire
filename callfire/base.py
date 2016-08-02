import base64
import sys
import json
import urllib
import urllib2


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

    def __init__(self, username, password):
        """API base.

        :param username: API username
        :param password: API password
        """
        self.username = username
        self.password = password

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
        query = query or dict()
        body = body or dict()

        url = '{}/{}?{}'.format(self.BASE_URL, path, urllib.urlencode(query))
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
            exception_type, value, traceback = sys.exc_info()
            exception_wrapper = CallFireError(wrapped_exc, str(wrapped_exc))
            raise CallFireError, exception_wrapper, traceback
