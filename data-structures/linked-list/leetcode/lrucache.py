class LRUCache:

    def __init__(self, capacity):
        '''Initialise LRUCache with fixed capacity 
        '''
        self.capacity = capacity


    def get(self, key: int) -> int:
        '''Return the value of the key if exist. Return -1 if does not
        '''
        pass

    def put(self, key: int, value: int) -> int:
        '''Puts key-value pair into the cache
        If key exists, update value of the key to new value
        If cache is full, evict least-recently-used key
        '''
        pass

class LFUCache:

    def __init__(self, capacity):
        '''Initialise LFUCache with fixed capacity
        '''
        self.capacity = capacity

    def get(self, key: int) -> int:
        '''Return the value of the key if exist. Return -1 if does not
        '''
        pass

    def put(self, key: int, value: int) -> int:
        '''Puts key-value pair into the cache
        If key exists, update value of the key to new value
        If cache is full, evict least-frequently-used key
        '''
        pass
