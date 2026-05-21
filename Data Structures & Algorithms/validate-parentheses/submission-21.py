class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for curr_bracket in s:
            if curr_bracket in hash_map:
                stack.append(curr_bracket)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if hash_map[top] != curr_bracket:
                    return False
            
        if len(stack) >= 1:
            return False
        return True