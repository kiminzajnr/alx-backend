#!/usr/bin/env python3
""" LRU Caching
"""
import collections
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ This class implements LRU caching"""
    def __init__(self):
        super().__init__()
        self.cache_data = collections.OrderedDict()

    def put(self, key, item):
        """ Adds item to dictionary with key key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # discard least recently used hear
            tup = self.cache_data.popitem(last=False)
            # print
            print("DISCARD: {}".format(tup[0]))

    def get(self, key):
        """ return value in cache linkey to key"""
        if key is None:
            return None
        try:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        except KeyError:
            return None
