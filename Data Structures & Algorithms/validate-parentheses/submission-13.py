class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for bracket in s:
            if brackets.get(bracket, 0):
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False

                topmost = stack.pop()
                if brackets[topmost] != bracket:
                    return False
                    
        if len(stack) == 0:
            return True
        else:
            return False