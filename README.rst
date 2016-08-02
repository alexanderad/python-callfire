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


Whenever low level exception occurs it is wrapped and re-raised as `CallFireError`,
while original traceback preserved and displayed and original exception is also
available for inspection::

    try:
        api.find_caller_ids()
    except CallFireError as e:
        print e.wrapped_exc

