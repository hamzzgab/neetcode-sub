class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:                
                if not stack:
                    return False 
                                                   
                top = stack.pop()
                if brackets[top] != bracket:
                    return False

        if stack:
            return False
        return True
