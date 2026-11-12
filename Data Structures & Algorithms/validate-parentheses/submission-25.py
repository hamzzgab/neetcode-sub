class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for bracket in s:
            if bracket not in mapping:
                stack.append(bracket)
            else:
                if not stack:
                    return False 

                open_bracket = stack.pop()
                if mapping[bracket] != open_bracket:
                    return False

        return not stack
