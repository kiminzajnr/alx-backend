#!/usr/bin/env python3
""" FIFOCache inherits from BasicCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ inherits from BasicCache
    """

    def put(self, key, item):
        """ add n item from cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_item_key = list(self.cache_data.keys())[0]
            del self.cache_data[discarded_item_key]
            print("DISCARD: {}".format(discarded_item_key))

    def get(self, key):
        """ get an item from cache"""
        if key is None:
            return None
        try:
            self.cache_data[key]
        except KeyError:
            return None
        return self.cache_data[key]
