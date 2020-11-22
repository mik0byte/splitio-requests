********************************************
Split.io Admin API wrapper
********************************************

.. image:: https://img.shields.io/pypi/v/splitio-requests.svg
   :alt: Current version

.. image:: https://img.shields.io/pypi/l/splitio-requests.svg
   :alt: License

.. image:: https://img.shields.io/pypi/pyversions/splitio-requests.svg
   :alt: PyPI - Python Version

.. image:: https://static.pepy.tech/personalized-badge/splitio-requests?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads
   :target: https://pepy.tech/project/splitio-requests
   :alt: Downloads count


Split.io is feature experimentation platform and it has it's public API,
allowing it's customers to interact with their resources.

splitio-requests package makes it easy to interact with Admin API by wrapping endpoint requests and providing
simplified way to access response data and much more.

-------------------

**Quick example on how to use it**

.. code-block:: python

    >>> admin_api = AdminAPI("ADMIN_API_TOKEN")
    >>> resp = admin_api.splits.get_split("awesome_split", "wsid-123")
    >>> resp.status_code
    200
    >>> resp.json()
    {"name": "awesome_split","description": "Great feature",...
    >>> resp.url
    'https://api.split.io/internal/api/v2/splits/ws/wsid-123/'
    >>> resp.headers
    '{"X-RATE-LIMIT":"12"...'
    >>> bool(resp) # When request was successful
    True


What's great about splitio-requests is that it handles Split.io Admin API throttling system with polling and retires.

Those functionalities are configured by default but changes can be made by the user if necessary.

**Other key features**

* Model classes for resources
* Schemas and serializers for payload data validation