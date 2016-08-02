python-callfire
===============

Thin wrapper around `CallFire API <https://developers.callfire.com/docs.html>`_.

Usage
-----
::

    from callfire import CallFireAPI

    api = CallFireAPI('username', 'password')
    response = api.send_calls(
        query=dict(defaultVoice='KATE'),
        body=dict(phoneNumber='+1234234234', liveMessage='Hi!')
    ).json()


