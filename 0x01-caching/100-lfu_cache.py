#!/usr/bin/env python3
"""
Implements a Least Frequently Used caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Represents a Least Frequently Used (LFU) caching mechanism, where
    the least frequently used items are removed when the cache limit is
    reached. Inherits from BaseCaching.
    """
    def __init__(self):
        """Initializes the LFU cache"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.key_freq = OrderedDict()

    def __reorder_items(self, key):
        """
        Reorders the items in the cache based on the least frequently
        used item.
        """
        freq = self.key_freq[key]
        self.key_freq[key] = freq + 1
        del self.cache_data[key]
        for k, v in self.key_freq.items():
            if v == freq:
                self.cache_data[k] = self.cache_data.pop(k)
        self.cache_data[key] = self[key]

    def put(self, key, item):
        """
        Adds an item to the cache.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.__reorder_items(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            lfu = min(self.key_freq, key=self.key_freq.get)
            self.key_freq.pop(lfu)
            self.cache_data.pop(lfu)
            print(f"DISCARD: {lfu}")
        self.cache_data[key] = item
        self.key_freq[key] = 0

    def get(self, key):
        """
        Retrieves an item from the cache by its key.
        """
        if key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
