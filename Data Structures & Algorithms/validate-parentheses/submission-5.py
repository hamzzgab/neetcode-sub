class Solution:
    def __init__(self):
        self._bracket_map = {
            '{': '}',
            '[': ']',
            '(': ')',
            '<': '>',
        }
        self._stack = []

    def isValid(self, expression: str) -> bool:
        for curr_bracket in expression:
            if curr_bracket == '[' or curr_bracket == '{' or curr_bracket == '(' or curr_bracket == '<':
                self._stack.append(curr_bracket)
            else:
                if not self._stack:
                    return False
                popped_bracket = self._stack.pop()

                if curr_bracket == ']' and popped_bracket != '[':
                    return False
                if curr_bracket == '}' and popped_bracket != '{':
                    return False
                if curr_bracket == ')' and popped_bracket != '(':
                    return False
                if curr_bracket == '>' and popped_bracket != '<':
                    return False

        if not self._stack:
            return True
        return False
