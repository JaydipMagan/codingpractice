class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []
        self.size = -1
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size+=1
        self.sorted_stack = sorted(self.stack)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.size-=1
        self.sorted_stack = sorted(self.stack)

    def top(self) -> int:
        return self.stack[self.size]
    
    def getMin(self) -> int:
        return self.sorted_stack[0]