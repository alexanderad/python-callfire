import base64
import json
import os
import unittest
import sys
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


class FakeResponse(object):

    def __init__(self, prepared):
        self._prepared = prepared
    def read(self):
        return self._prepared.data


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.base = callfire_base.BaseAPI('username', 'password')
        self.base.BASE_URL = 'base_url'

    def test_base_attrs(self):
        self.assertEqual(self.base.username, 'username')
        self.assertEqual(self.base.password, 'password')

    def test_request(self):
        fake_request = flexmock()
        fake_prepared = flexmock()
        (flexmock(fake_request)
         .should_receive('prepare')
         .and_return(fake_prepared))
        fake_response = flexmock(read=lambda: b'{"success": true}')
        (flexmock(callfire_base)
         .should_receive('urlopen')
         .with_args(fake_prepared)
         .and_return(fake_response))

        for test_method in (self.base._get,
                            self.base._put,
                            self.base._post,
                            self.base._delete):
            response = test_method(fake_request)
            self.assertDictEqual(response.json(), dict(success=True))

    def test_exception_wrapper_wraps_url_error(self):
        path, query, body = '/path', dict(fields='id'), dict(data='data')

        fake_request = flexmock(
            prepare=flexmock(),
            path=flexmock(),
            query=flexmock(),
            body=flexmock()
        )

        (flexmock(callfire_base)
         .should_receive('urlopen')
         .and_raise(callfire_base.URLError('Internal error')))

        with self.assertRaises(callfire_base.CallFireError):
            self.base._open_request(fake_request, 'GET')

    def test_exception_wrapper_wraps_http_error(self):
        fake_request = flexmock(
            prepare=flexmock(),
            path=flexmock(),
            query=flexmock(),
            body=flexmock()
        )
        fake_exception_fp = StringIO('{"error": "Bad Request"}')
        fake_exception_fp.seek(0)
        (flexmock(callfire_base)
         .should_receive('urlopen')
         .and_raise(
            HTTPError('url', 400, 'Bad Request', {}, fake_exception_fp)))

        with self.assertRaises(callfire_base.CallFireError) as cm:
            self.base._open_request(fake_request, 'GET')

        e = cm.exception
        self.assertIsInstance(e, callfire_base.CallFireError)
        self.assertIsInstance(e.wrapped_exc, HTTPError)
        self.assertEqual(
            str(e), 'HTTP Error 400: Bad Request: {"error": "Bad Request"}')

    def test_get_auth_header(self):
        expected_auth_header = 'Basic {}'.format(
            base64.b64encode(
                '{}:{}'.format(
                    self.base.username, self.base.password
                ).encode()
            ).decode()
        )
        self.assertEqual(self.base._get_auth_header(), expected_auth_header)

    def test_json_request(self):
        request = callfire_base.JSONRequest(path="/test", body=[42])

        custom_urlopen = lambda prepared: FakeResponse(prepared)
        flexmock(callfire_base, urlopen=custom_urlopen)

        response = self.base._open_request(request, 'GET')
        self.assertEqual(response.json(), [42])

    def test_multipart_request(self):

        with open(os.__file__, 'rb') as stream:
            request = callfire_base.MultipartRequest(
                path="/test",
                payload=stream)

            custom_urlopen = lambda prepared: FakeResponse(prepared)
            flexmock(callfire_base, urlopen=custom_urlopen)

            response = self.base._open_request(request, 'POST')

        content = response.read()

        with open(os.__file__, 'rb') as stream:
            payload = callfire_base.MultipartRequest.generate_multipart(stream)

        self.assertEqual(payload, content)


if __name__ == '__main__':
    unittest.main()
