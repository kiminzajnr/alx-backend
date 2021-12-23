#!/usr/bin/env python3
""" MRU Caching"""
import collections
BaseCaching = __import__('0-basic_cache').BaseCaching


class MRUCache(BaseCaching):
    """ This class inherits from BaseCaching base class"""
    keys = []

    def put(self, key, item):
        """ Adds an item to a dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        if key not in self.keys:
            MRUCache.keys.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # discard the most recently used item
            discard = MRUCache.keys.pop(-2)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Return value linked to a key"""
        if key is None:
            return None
        try:
            if key in MRUCache.keys:
                MRUCache.keys.append(
                    MRUCache.keys.pop(MRUCache.keys.index(key)))
            return self.cache_data[key]
        except KeyError:
            return None
