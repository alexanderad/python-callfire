python-callfire
===============

Thin wrapper around `CallFire API <https://developers.callfire.com/docs.html>`_.
API wrapper definitions are generated automatically based on Swagger JSON spec.

Usage
-----
::

    In [1]: from callfire import CallFireAPI
    In [2]: api = CallFireAPI('<api-app-username>', '<api-app-password>')

    In [2]: api.get_account().json()
    Out[2]:
    {u'email': u'your-email@your-domain.com',
     u'firstName': u'John',
     u'id': 700321776,
     u'lastName': u'Smith',
     u'name': u'Metacortex',
     u'permissions': [u'ACCOUNT_HOLDER']}

     In [3]: api.get_call?
     Signature: api.get_call(id, query=None)
     Docstring:
     Find a specific call.

     Returns a single Call instance for a given call id.

     :path integer id: Id of call
     :query string fields: Limit fields returned. E.g. fields=id,name or
     fields=items(id,name)
     File:      ~/Code/Python/python-callfire/callfire/callfire_v2.py
     Type:      instancemethod

     In [4]: api.send_texts(body=[dict(phoneNumber='13408887345', message='Hi!')]).json()
     Out[4]:
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

