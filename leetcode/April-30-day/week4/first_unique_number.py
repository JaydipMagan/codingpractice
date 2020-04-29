import collections
class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
    
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.freq = {}
        self.queue = []
        for num in nums:
            self.add(num)
        
    def showFirstUnique(self) -> int:
        while self.queue and self.freq[self.queue[0]]>1:
            self.queue.pop(0)#remove first element
            
        return self.queue[0] if len(self.queue)!=0 else -1
                

    def add(self, value: int) -> None:
        if value not in self.freq.keys():
            self.freq[value] = 1
            self.queue.append(value)
        else:
            self.freq[value] +=1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)