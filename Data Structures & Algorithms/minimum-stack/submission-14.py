class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_stack.append(val)
            return
        min_val = self.min_stack[-1]
        self.stack.append(val)
        self.min_stack.append(min(min_val, val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
