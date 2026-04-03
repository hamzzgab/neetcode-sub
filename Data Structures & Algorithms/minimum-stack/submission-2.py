class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.top_of_stack = -1

    def push(self, val: int) -> None:
        minimum_value  = min(val, self.min_stack[-1] if self.min_stack else val)
        self.stack.append(val)
        self.min_stack.append(minimum_value)
        self.top_of_stack += 1

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.top_of_stack -= 1

    def top(self) -> int:
        return self.stack[self.top_of_stack]

    def getMin(self) -> int:
        return self.min_stack[self.top_of_stack]