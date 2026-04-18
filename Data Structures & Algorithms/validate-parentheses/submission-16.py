class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
                print(f'OPEN: {stack}')
            else:
                if not stack:
                    return False

                curr = stack.pop()
                if open_brackets[curr] != bracket:
                    return False
                
        if not stack:
            return True
        return False
                