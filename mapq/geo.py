"""
Geocode locations using the Mapquest Geocoding API.

Documentation:  http://www.mapquestapi.com/geocoding/
"""

import os
from urllib import unquote

import requests as req
from simplejson import loads


class Geo(object):
    """A simple Mapquest Geocoding API wrapper."""

    def __init__(self, api_key=None, endpoint=None):
        self._set_key(api_key)
        self._set_endpoint(endpoint)

    def _set_key(self, api_key):
        """Configure the instance's Mapquest API key."""
        if not api_key:
            if 'MAPQUEST_API_KEY' in os.environ:
                api_key = os.environ['MAPQUEST_API_KEY']
            else:
                api_key = ''
        self.api_key = unquote(api_key)

    def _set_endpoint(self, endpoint):
        """Configure the instance's Mapquest endpoint."""
        if not endpoint:
            if 'MAPQUEST_ENDPOINT' in os.environ:
                endpoint = os.environ['MAPQUEST_ENDPOINT']
            else:
                endpoint = 'http://www.mapquestapi.com/geocoding/v1'
        self.endpoint = endpoint

    def get(self, path, **kwargs):
        """Perform a get request."""
        if 'key' not in kwargs and 'api_key' not in kwargs:
            kwargs['key'] = self.api_key
        url = '/'.join((self.endpoint, path))
        request = req.get(url, params=kwargs)
        self.request = request
        results = loads(request.text)['results']
        return results

    def address(self, name, **kwargs):
        """
        Geocode an address.

        >>> Geo().address('155 9th St San Francisco, CA')
        """
        kwargs['location'] = name
        results = self.get('address', **kwargs)
        locations = results[0]['locations']
        return locations

    def batch(self, *locations, **kwargs):
        """Batch geolocate a number of addresses."""
        kwargs['location'] = locations
        return self.get('batch', **kwargs)

    def reverse(self, lat, lng, **kwargs):
        """
        Reverse geocode latitude and longitude coordinates.

        >>> Geo().reverse(37.775002, -122.418297)
        """
        kwargs['lat'] = lat
        kwargs['lng'] = lng
        return self.get('reverse', **kwargs)

    def latlng(self, address, **kwargs):
        """
        Return the first pair of latitude and longitude coordinates for a
        given address.

        >>> Geo().latlng('155 9th St San Francisco, CA')
        """
        results = self.address(address, **kwargs)
        location = results[0]['displayLatLng']
        return location
