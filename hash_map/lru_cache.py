# https://leetcode.com/problems/lru-cache

"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

class LRUCache:
    def __init__(self, capacity: int):
        self.max_cap = capacity
        self.lru = []
        self.store = {}
        self.is_update = False

    def mru(self, key: int):
        self.lru.remove(key)
        self.lru.append(key)

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        
        # move to end (most recently used)
        self.mru(key)
        return self.store[key]


    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.is_update = True

        if not self.is_update and len(self.store) + 1 > self.max_cap:
            lru_key = self.lru.pop(0)
            del self.store[lru_key]

            self.store.update({ key: value })
            self.lru.append(key)

        else:
            self.store.update({ key: value })
            
            if self.is_update:
                self.mru(key)
                self.is_update = False
            else:
                self.lru.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)