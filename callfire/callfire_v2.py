from .base import BaseAPI


class CallFireAPIVersion2(BaseAPI):
    """CallFire API v2 wrapper.

    Wrapped methods match documented methods:
     * query matches query params
     * body matches body params
     * method args match path params
    """
    #: Base API url
    BASE_URL = 'https://api.callfire.com/v2'

    def send_calls(self, query=None, body=None):
        return self._post('calls', query, body)

    def send_texts(self, query=None, body=None):
        return self._post('texts', query, body)

    def add_sound_tts(self, query=None, body=None):
        return self._post('campaigns/sounds/tts', query, body)

    def find_sound(self, id, query=None):
        return self._get('campaigns/sounds/{}'.format(id), query)

    def download_mp3_sound(self, id):
        return self._get('campaigns/sounds/{}.mp3'.format(id))

    def find_caller_ids(self):
        return self._get('me/callerids')

    def create_caller_id(self, caller_id):
        return self._post('me/callerids/{}'.format(caller_id))

    def verify_caller_id(self, caller_id, body):
        return self._post(
            'me/callerids/{}/verification-code'.format(caller_id), body=body)


# alias current version
CallFireAPI = CallFireAPIVersion2
