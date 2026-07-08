class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [float('inf')]
        
    def push(self, val: int) -> None:
        v = min(self.minStack[-1], val)
        self.minStack.append(v)
        self.stack.append(val)
    
    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
