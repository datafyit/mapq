mapq
====

An easy-to-use wrapper for the [Mapquest Geocoding API](http://www.mapquestapi.com/geocoding/).

Make sure to register for [Mapquest API key](http://developer.mapquest.com/).


Installation
------------

    pip install mapq


Settings
--------

The easiest way to use `mapq` is by setting the `MAPQUEST_API_KEY`
environment variable in your local environment.

    export MAPQUEST_API_KEY="my_api_key"


Usage
-----

There are two ways of interacting with `mapq`'s API.

```python
>>> import mapq

>>> mapq.key('my_api_key')

>>> mapq.address('155 9th St San Francisco, CA')
[{'lots': {'of': 'results'}}, ...]

>>> mapq.batch('94103', '1 Infinity Loop Cupertino', 'Yerba Buena Park')
[{'multiple': 'locations'}, ...]

>>> mapq.geocode('155 9th St San Francisco, CA')
{'single': {'geocode': 'result'}}

>>> mapq.reverse(37.775002, -122.418297)
{'looks': {'like': '155 9th St'}}

>>> mapq.latlng('155 9th St San Francisco, CA')
{'lat': 37.775002, 'lng': -122.418297}
```

Alternatively, you can also use the Mapquest API by interacting with the `Geo`
class.

```python
>>> from mapq import Geo
>>> g = Geo('my_api_key')

>>> g.address('155 9th St San Francisco, CA')
[{'lots': {'of': 'results'}}, ...]

>>> g.batch('94103', '1 Infinity Loop Cupertino', 'Yerba Buena Park')
[{'multiple': 'locations'}, ...]

>>> g.reverse(37.775002, -122.418297)
{'looks': {'like': '155 9th St'}}

>>> g.latlng('155 9th St San Francisco, CA')
{'lat': 37.775002, 'lng': -122.418297}
```


Specify a Mapquest endpoint if desired. This allows the Open Data endpoint to be used instead of the licensed endpoint.


```python
>>> import mapq

>>> mapq.endpoint('http://open.mapquestapi.com/geocoding/v1')
```

Can also be set when interacting with the `Geo` class.

```python
>>> from mapq import Geo
>>> g = Geo('my_api_key', 'http://open.mapquestapi.com/geocoding/v1')
```

