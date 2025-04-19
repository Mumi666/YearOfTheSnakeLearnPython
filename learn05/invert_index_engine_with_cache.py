import pylru

from learn05.invert_index_engine import InvertIndexEngine


class LRUCache(object):
    def __init__(self, size=32):
        self.cache = pylru.lrucache(size)
    def get(self, key):
        result = self.cache[key]
        return result
    def set(self, key, value):
        self.cache[key] = value
    def remove(self, key):
        del self.cache[key]
    def has(self, key):
        return key in self.cache

class InvertIndexEngineWithCache(InvertIndexEngine, LRUCache):
    def __init__(self):
        super(InvertIndexEngineWithCache, self).__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print('hit cache')
            return self.get(query)

        result = super(InvertIndexEngineWithCache, self).search(query)
        self.set(query, result)
        return result

