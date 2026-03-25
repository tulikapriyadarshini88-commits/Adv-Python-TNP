from collections import OrderedDict

class LRU:
    def __init__(self, cap):
        self.cache = OrderedDict()
        self.cap = cap

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, val):
        self.cache[key] = val
        self.cache.move_to_end(key)
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)