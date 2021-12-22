#!/usr/bin/env python3
""" LIFOCache inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Inherits from BaseCaching
    """
    last_key = ""

    def put(self, key, item):
        """ Add an item to a dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(LIFOCache.last_key))
            del self.cache_data[LIFOCache.last_key]
        LIFOCache.last_key = key

    def get(self, key):
        """ Return value linked to key
        """
        if key is None:
            return None
        try:
            self.cache_data[key]
        except KeyError:
            return None
        return self.cache_data[key]
