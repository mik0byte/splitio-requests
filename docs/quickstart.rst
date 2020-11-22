.. _quick_start:

**********
Quickstart
**********


This guide will walk you through the basics of using Admin API. models and serializers.

Here is the list of :ref:`Currently supported endpoints`.

Getting Started
---------------

First, make sure that:

* splitio-requests is :ref:`installed <install>`

Now import AdminApi manager class and then create an object from it by passing Split.io Admin API key that you have
generated from Split's admin panel.

.. code-block:: python

     >>> from splitiorequests import AdminAPI
     >>> admin_api = AdminAPI('VerySecretToken')

Accessing Admin API endpoints
-----------------------------

You can access any API resource from AdminAPI object that has been created.

.. code-block:: python

     >>> workspaces_resp = admin_api.environments.get_environments("wsid-123")
     >>> if workspaces_resp:
     ...    print(workspaces_resp.json())
     >>> else:
     ...    print(f"Error status code: {workspaces_resp.status_code}, Message: {workspaces_resp.json()}")


Creating new resource instance with model classes
-------------------------------------------------

To create a new split, split definition and any other resource you need to create a python dict/json file with
correct structure and pass in as an argument in admin api method. But that can be overhead to keep and maintain those big and nested dictionaries in your code.
For that there are available models for all resources that can help you to create data using classes.

.. code-block:: python

     >>> from splitiorequests.models.splits.split import Split
     >>> new_split = Split('split_name', 'Cool description')


Data Models validators/serializers and parsers
----------------------------------------------

After you have created your resource model object you can easily dump it into python dictionary with serializers helper functions.

.. code-block:: python

     >>> from splitiorequests.serializers.splits import dump_split
     >>> new_split_dict = dump_split(new_split)
     >>> admin_api.splits.create_split('wsid-123', 'traffic-123', new_split_dict)

If you have a payload that is python dictionary then you can validate it with load helper functions, which will return you model object.

.. code-block:: python

     >>> from splitiorequests.serializers.splits import load_split
     >>> split_dict = {"name":"new_split","description":"description"}
     >>> new_split_obj = dump_split(new_split)
