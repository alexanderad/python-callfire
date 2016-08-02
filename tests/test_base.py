import base64
import json
import unittest
import urllib2
from StringIO import StringIO

from flexmock import flexmock

from . import callfire_base


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.base = callfire_base.BaseAPI('username', 'password')
        self.base.BASE_URL = 'base_url'

    def test_base_response_json(self):
        test_json = dict(key='value')
        response = callfire_base.BaseResponse(StringIO(json.dumps(test_json)))
        self.assertDictEqual(response.json(), test_json)

    def test_base_attrs(self):
        self.assertEqual(self.base.username, 'username')
        self.assertEqual(self.base.password, 'password')

    def test_request(self):
        path = 'path'
        query = dict(fields='id')
        body = dict(data='data')

        expected_url = 'base_url/path?fields=id'
        expected_data = json.dumps(body)
        expected_headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic {}'.format(
                base64.encodestring(
                    '{}:{}'.format(self.base.username, self.base.password)
                ).strip()
            )
        }

        fake_request = flexmock()
        (flexmock(urllib2)
         .should_receive('Request')
         .with_args(expected_url, expected_data, expected_headers)
         .and_return(fake_request))

        fake_response = flexmock()
        (flexmock(urllib2)
         .should_receive('urlopen')
         .with_args(fake_request)
         .and_return(fake_response))

        response = self.base._request(path, query, body, 'POST')
        self.assertIsInstance(response, callfire_base.BaseResponse)
        self.assertEqual(response._response, fake_response)

    def test_post(self):
        path = 'path'
        query = dict(fields='id')
        body = dict(data='data')

        (flexmock(self.base)
         .should_receive('_request')
         .with_args(path, query, body, 'POST'))

        self.base._post(path, query, body)

    def test_get(self):
        path = 'path'
        query = dict(fields='id')
        body = dict(data='data')

        (flexmock(self.base)
         .should_receive('_request')
         .with_args(path, query, body, 'GET'))

        self.base._get(path, query, body)

    def test_delete(self):
        path = 'path'
        query = dict(fields='id')
        body = dict(data='data')

        (flexmock(self.base)
         .should_receive('_request')
         .with_args(path, query, body, 'DELETE'))

        self.base._delete(path, query, body)

    def test_put(self):
        path = 'path'
        query = dict(fields='id')
        body = dict(data='data')

        (flexmock(self.base)
         .should_receive('_request')
         .with_args(path, query, body, 'PUT'))

        self.base._put(path, query, body)

if __name__ == '__main__':
    unittest.main()
