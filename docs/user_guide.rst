.. _user_guide:

User Guide
============
User Guide on how to setup adminapi and use it's properties to access endpoints, resources models, validators/serializers

Currently supported endpoints
-----------------------------

* **Workspaces**
    * `Get Workspaces <https://docs.split.io/reference#get-workspaces>`_
* **Environments**
    * `Get Environments <https://docs.split.io/reference#get-environments>`_
    * `Create Environment <https://docs.split.io/reference#create-environment>`_
    * `Delete Environment <https://docs.split.io/reference#delete-environment>`_
    * `Update Environment <https://docs.split.io/reference#update-environment>`_
* **Traffic Types**
    * `Get Traffic Types <https://docs.split.io/reference#get-traffic-types>`_
* **Splits**
    * `Create Split <https://docs.split.io/reference#create-split>`_
    * `List Splits <https://docs.split.io/reference#list-splits>`_
    * `Get Split <https://docs.split.io/reference#get-split>`_
    * `Delete Split <https://docs.split.io/reference#delete-split>`_
    * `Update Split Description <https://docs.split.io/reference#update-split-description>`_
    * `Create Split Definition in Environment <https://docs.split.io/reference#create-split-definition-in-environment>`_
    * `Get Split Definition in Environment <https://docs.split.io/reference#get-split-definition-in-environment>`_
    * `Partial Update Split Definition in Environment <https://docs.split.io/reference#partial-update-split-definition-in-environment>`_
    * `Full Update Split Definition in Environment <https://docs.split.io/reference#full-update-split-definition-in-environment>`_
    * `Remove Split Definition in Environment <https://docs.split.io/reference#remove-split-definition-from-environment>`_
    * `List Split Definitions in Environment <https://docs.split.io/reference#lists-split-definitions-in-environment>`_
    * `Kill Split in Environment <https://docs.split.io/reference#kill-split-in-environment>`_
    * `Restore Split in Environment <https://docs.split.io/reference#restore-split-in-environment>`_
* **Tags**
    * `Associate Tags <https://docs.split.io/reference#associate-tags>`_


Admin API Manager class
-----------------------

This is the main class that allows you to access all endpoints and all API throttle handling mechanism is being instantiated here.

You can simply pass only API key and let this lib to handle all dirty things for you can set your custom settings.

It will append all necessary headers to all requests but you can add some headers(if there's a need) "Manager object wide".
What "Manager object wide" really means?
All future requests with it's object will include the headers you provided. If you don't want to do that you can pass headers with every
request method as an argument, which will be applied only to that one request.

.. code-block:: python

     >>> from splitiorequests import AdminAPI
     >>> admin_api = AdminAPI('VerySecretToken', headers={'CustomHeader': 'value'})

You can also specify hostname, if for some reason you use another version of Split's API(current is v2).

.. code-block:: python

     >>> from splitiorequests import AdminAPI
     >>> admin_api = AdminAPI('VerySecretToken', hostname='https://new-api-URL/api/vX')

Next important thing is session object.
New session object will be created if not passed in during instantiation.

Split's API has a throttling system, which blocks requests after doing few requests and you need to wait for a while and try again.
There's retry implemented with Session object that is being created automatically.

If you do a request and response status code is in this list => 429, 500, 502, 503, 504 then it will retry again and again until succeeds.

Max retry by default is 10, but you can change it. But instead of retrying without waiting for a while which will lead to failures,
it will sleep according to this algorithm - {backoff factor} * (2 ** ({number of total retries} - 1)).

You can change all default values of retry mechanism as well.

.. code-block:: python

     >>> from splitiorequests import AdminAPI
     >>> admin_api = AdminAPI('VerySecretToken', retries=5, backoff_factor=0.2, status_forcelist=(429,))


AdminAPI properties or how to access endpoints
----------------------------------------------

There are available properties on AdminAPI's object.

* workspaces
* environments
* traffictypes
* splits
* tags


In Split's API there are endpoints that return list of items. Their methods here are python generators, where you call the function
pass in optional pagination arguments and it will iterate over pages and return you generator objects.

Example:

.. code-block:: python

     >>> for get_workspaces_resp in admin_api.workspaces.get_workspaces:
     ...    if get_workspaces_resp:
     ...        for workspace in get_workspaces_resp.json()['objects']:
     ...            print(f"Workspace: {workspace['name']}")
     ...    else:
     ...        print(f"Error status code: {get_workspaces_resp.status_code}, Message: {get_workspaces_resp.json()}")

You can also specify *limit* and *offset* parameters.

.. code-block:: python

     >>> workspaces_gen = admin_api.workspaces.get_workspaces(offset=10, limit=5)



All other endpoints that are not returning list of items, they return *Response* object.

Example:

.. code-block:: python

     >>> get_split_resp = admin_api.splits.create_split('wsid-123', 'traffic-id-123', {'name': 'awesome-feature'})
     >>> print(get_split_resp.status_code)
     200
     >>> print(get_split_resp.json())
     {"name": "awesome-feature", "description": "","trafficType": {"id": "traffic-id-123","name": "user"}}

.. seealso::

    Look at :ref:`API reference <admin_api_properties>` for more available methods.

Create new instances with models
--------------------------------

Whenever you are creating a new split, split definitions etc. you need to have a payload in form of python dict.
And to write that whole nested structure by hand all keep it in the code can take a lot of time and against programming principles.
So there are model classes that allow you to easily create payload.

Example:

.. code-block:: python

     >>> from splitiorequests.models.splits.split import Split
     >>> new_split = Split('split_name', 'Cool description')

.. seealso::

    Look at :ref:`API reference <models_classes>` for more available model classes.


Validate your payload or dump model class to python dict
--------------------------------------------------------

Another thing that we need is after creating a new split or split definition model class we need to dump them to python dict
so we can pass it in endpoint method as a payload.
We can do that with helper serializer functions.

.. code-block:: python

     >>> from splitiorequests.serializers.splits import dump_split
     >>> new_split_dict = dump_split(new_split)

Or if we have a json that contains payload or a python dictionary and we want to validate the payload we can do that with load functions

.. code-block:: python

     >>> from splitiorequests.serializers.splits import load_split
     >>> split_dict = {'name': 'awesome-feature', 'description': 'A long desc...'}
     >>> split_obj = load_split(split_dict)

This will raise an exception if there are mistakes in payload, if there are no mistakes then it will return Split model object.

You can also pass in optional handler argument to load function which will simply ignore and remove unknown fields.

.. code-block:: python

     >>> from splitiorequests.serializers.splits import load_split
     >>> split_dict = {'name': 'awesome-feature', 'description': 'A long desc...', 'unknown_field': 'value'}
     >>> split_obj = load_split(split_dict, 'exclude')
     Split(name='awesome-feature', description='A long desc...', trafficType=None, creationTime=None, tags=None)

.. seealso::

    Look at :ref:`API reference <serializer_validators>` for more available serializers/validators.
