#!/usr/bin/env python3
""" BasicCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching
    """

    def put(self, key, item):
        """ Add an item to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key is None:
            return None
        try:
            self.cache_data[key]
        except KeyError:
            return None
        return self.cache_data[key]
