from inspect import stack
from traceback import print_tb


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element: str):
        self.stack.append(element)

    def pop(self) -> int:
        if self.__len__() == 0:
            return -1
        return self.stack.pop()

    def __len__(self):
        if not self.stack:
            return 0
        return len(self.stack)

    @property
    def get_stack(self): return self.stack


class Solution(Stack):
    def __init__(self):
        self._bracket_map = {'{': '}', '[': ']', '(': ')', '<': '>'}
        super().__init__()

    def isValid(self, expression: str) -> bool:
        for curr_bracket in expression:
            if curr_bracket in self._bracket_map:
                self.push(curr_bracket)
            else:
                popped_bracket = self.pop()
                if popped_bracket == -1:
                    return False
                if self._bracket_map[popped_bracket] != curr_bracket:
                    return False

        return len(self.stack) == 0