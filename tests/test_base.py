import base64
import json
import unittest
try:
    # py2
    from urllib2 import HTTPError
    from StringIO import StringIO
except ImportError:
    # py3
    from urllib.error import HTTPError
    from io import StringIO


from flexmock import flexmock

from . import callfire_base


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.base = callfire_base.BaseAPI('username', 'password')
        self.base.BASE_URL = 'base_url'

    def test_base_attrs(self):
        self.assertEqual(self.base.username, 'username')
        self.assertEqual(self.base.password, 'password')

    def test_request(self):
        path, query, body = '/path', dict(fields='id'), dict(data='data')

        expected_url = 'base_url/path?fields=id'
        expected_data = json.dumps(body)
        expected_headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic {}'.format(
                base64.b64encode(
                    '{}:{}'.format(
                        self.base.username, self.base.password).encode('utf-8')
                ).strip()
            )
        }

        fake_request = flexmock()
        (flexmock(callfire_base)
         .should_receive('Request')
         .with_args(expected_url, expected_data, expected_headers)
         .and_return(fake_request))

        fake_response = flexmock(read=lambda: '{"success": true}')
        (flexmock(callfire_base)
         .should_receive('urlopen')
         .with_args(fake_request)
         .and_return(fake_response))

        response = self.base._request(path, query, body, 'POST')
        self.assertDictEqual(response.json(), dict(success=True))

    def test_post(self):
        path, query, body = '/path', dict(fields='id'), dict(data='data')

        (flexmock(self.base)
         .should_receive('_request')
         .with_args(path, query, body, 'POST'))

        self.base._post(path, query, body)

    def test_get(self):
        path, query, body = '/path', dict(fields='id'), dict(data='data')

        (flexmock(self.base)
         .should_receive('_request')
         .with_args(path, query, body, 'GET'))

        self.base._get(path, query, body)

    def test_delete(self):
        path, query, body = '/path', dict(fields='id'), dict(data='data')

        (flexmock(self.base)
         .should_receive('_request')
         .with_args(path, query, body, 'DELETE'))

        self.base._delete(path, query, body)

    def test_put(self):
        path, query, body = '/path', dict(fields='id'), dict(data='data')

        (flexmock(self.base)
         .should_receive('_request')
         .with_args(path, query, body, 'PUT'))

        self.base._put(path, query, body)

    def test_exception_wrapper_wraps_url_error(self):
        path, query, body = '/path', dict(fields='id'), dict(data='data')

        fake_request = flexmock()
        (flexmock(callfire_base)
         .should_receive('Request')
         .and_return(fake_request))

        (flexmock(callfire_base)
         .should_receive('urlopen')
         .and_raise(callfire_base.URLError('Internal error')))

        with self.assertRaises(callfire_base.CallFireError):
            self.base._request(path, query, body, 'POST')

    def test_exception_wrapper_wraps_http_error(self):
        path, query, body = '/path', dict(fields='id'), dict(data='data')

        fake_request = flexmock()
        (flexmock(callfire_base)
         .should_receive('Request')
         .and_return(fake_request))

        fake_exception_fp = StringIO('{"error": "Bad Request"}')
        fake_exception_fp.seek(0)
        (flexmock(callfire_base)
         .should_receive('urlopen')
         .and_raise(
            HTTPError('url', 400, 'Bad Request', {}, fake_exception_fp)))

        with self.assertRaises(callfire_base.CallFireError) as cm:
            self.base._request(path, query, body, 'POST')

        e = cm.exception
        self.assertIsInstance(e, callfire_base.CallFireError)
        self.assertIsInstance(e.wrapped_exc, HTTPError)
        self.assertEqual(
            str(e), 'HTTP Error 400: Bad Request: {"error": "Bad Request"}')


if __name__ == '__main__':
    unittest.main()
