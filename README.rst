python-callfire
===============
.. image:: https://travis-ci.org/iMedicare/python-callfire.svg?branch=master
    :target: https://travis-ci.org/alexanderad/python-callfire

.. image:: https://img.shields.io/pypi/v/python-callfire.svg
    :target: https://pypi.python.org/pypi/python-callfire

Thin wrapper in Python which implements CallFire v2 interface definitions based on Swagger specification.

Usage
-----
Python method names follow `CallFire's API <https://developers.callfire.com/docs.html>`_.
Wrapper does not introduce any additional complexity or conventions above those defined in original API,
which makes usage pretty straightforward:

.. code-block:: python

    >>> from callfire import CallFireAPI
    >>> api = CallFireAPI('<api-app-username>', '<api-app-password>')

    >>> api.get_account().json()
    {
        u'email': u'your-email@your-domain.com',
        u'firstName': u'John',
        u'id': 700321776,
        u'lastName': u'Smith',
        u'name': u'Metacortex',
        u'permissions': [u'ACCOUNT_HOLDER']
    }

    >>> text = dict(phoneNumber='13408887345', message='Hi!')
    >>> api.send_texts(body=[text]).json()
    {
        u'items': [{
            u'batchId': 11428003374,
            u'campaignId': 60000313259,
            u'contact': {
                u'id': 152100378045,
                u'properties': {
                    u'UNDEFINED': u'13471521003'
                }
            },
            u'created': 1470222349000,
            u'finalTextResult': u'SENT',
            u'fromNumber': u'67076',
            u'id': 1038052003407,
            u'inbound': False,
            u'message': u'Hi!',
            u'modified': 1470222348000,
            u'records': [{
                u'billedAmount': 1.0,
                u'finishTime': 1470222349000,
                u'id': 579287900394,
                u'message': u'Hi!',
                u'textResult': u'SENT'
            }],
            u'state': u'FINISHED',
            u'toNumber': u'13408887345'
        }]
    }

    >>> broadcast = dict(
        fromNumber='13471521003',
        labels=['via-api'],
        name='Test voice broadcast'),
        answeringMachineConfig='AM_AND_LIVE',
        recipients=[dict(phoneNumber='(347) 1521003')],
        sounds=dict(
            liveSoundText='Voice message',
            machineSoundText='Voice message'
        )
    )
    >>> api.create_call_broadcast(query=dict(start=True), body=broadcast).json()
    {u'id': 13750937003}

    >>> api.get_call_broadcast(13750937003).json()
    {
        u'id': 13750937003,
        ...
        u'status': u'FINISHED'
    }


Error Handling
--------------
Whenever low level exception occurs it is wrapped and re-raised as `CallFireError`,
while original traceback preserved and displayed and original exception is also
available for inspection under `wrapped_exc` attribute.

Documentation
-------------
Generated python methods do contain docstrings with described query and body params.
Official API documentation is available at `developers.callfire.com <https://developers.callfire.com/docs.html>`_.
