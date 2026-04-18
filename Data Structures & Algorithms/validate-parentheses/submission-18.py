class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '{', '[']
        stack = []

        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
                print(f'OPEN: {stack}')
            else:
                if not stack:
                    return False

                curr = stack.pop()
                if bracket == '}' and curr != '{':
                    return False
                if bracket == ')' and curr != '(':
                    return False
                if bracket == ']' and curr != '[':
                    return False
                
        if not stack:
            return True
        return False
                