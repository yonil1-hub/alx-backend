#!/usr/bin/env python3
"""Last-In First-Out caching module.
"""
from collections import OrderedDict
from typing import Optional

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self) -> None:
        """Initializes the cache."""
        super().__init__()
        self.cache_data: OrderedDict = OrderedDict()

    def put(self, key: str, item: str) -> None:
        """Adds an item in the cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {last_key}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key: str) -> Optional[str]:
        """Retrieves an item by key."""
        return self.cache_data.get(key, None)
