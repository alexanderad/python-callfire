python-callfire
===============
.. image:: https://travis-ci.org/iMedicare/python-callfire.svg?branch=master
    :target: https://travis-ci.org/iMedicare/python-callfire

Thin wrapper around `CallFire API <https://developers.callfire.com/docs.html>`_.
API wrapper definitions are generated automatically based on Swagger JSON spec.


Usage
-----
.. code-block:: python

    >>> from callfire import CallFireAPI
    >>> api = CallFireAPI('<api-app-username>', '<api-app-password>')

    >>> api.get_account().json()
    {u'email': u'your-email@your-domain.com',
     u'firstName': u'John',
     u'id': 700321776,
     u'lastName': u'Smith',
     u'name': u'Metacortex',
     u'permissions': [u'ACCOUNT_HOLDER']}

    >>> api.send_texts(body=[dict(phoneNumber='13408887345', message='Hi!')]).json()
    {u'items': [{u'batchId': 11428003374,
        u'campaignId': 60000313259,
        u'contact': {u'id': 152100378045,
        u'properties': {u'UNDEFINED': u'13471521003'}},
        u'created': 1470222349000,
        u'finalTextResult': u'SENT',
        u'fromNumber': u'67076',
        u'id': 1038052003407,
        u'inbound': False,
        u'message': u'Hi!',
        u'modified': 1470222348000,
        u'records': [{u'billedAmount': 1.0,
          u'finishTime': 1470222349000,
          u'id': 579287900394,
          u'message': u'Hi!',
          u'textResult': u'SENT'}],
        u'state': u'FINISHED',
        u'toNumber': u'13408887345'}]}


Whenever low level exception occurs it is wrapped and re-raised as `CallFireError`,
while original traceback preserved and displayed and original exception is also
available for inspection.

