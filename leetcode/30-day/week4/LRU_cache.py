import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.vals = OrderedDict() # hashmap but with ordering for O(1)
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.vals:
            return -1
        else:
            self.vals.move_to_end(key)
            return self.vals[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.vals:
            if len(self.vals)>=self.capacity:
                self.vals.popitem(last=False) # removee first item
        else:
            self.vals.move_to_end(key)
        self.vals[key] = value
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)