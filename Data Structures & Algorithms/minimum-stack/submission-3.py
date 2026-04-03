class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []        

    def push(self, val: int) -> None:
        min_val = self.getMin()        
        self.min_stack.append(min(min_val, val))
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return float('inf')
        return self.min_stack[-1]
        
