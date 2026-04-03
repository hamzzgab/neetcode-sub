class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '{': '}',
            '(': ')',
            '[': ']'
        }

        stack = []
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
                print(stack)
            else:
                if len(stack) == 0:
                    return False

                popped_bracket = stack.pop()
                print(popped_bracket)

                if brackets[popped_bracket] != bracket:
                    return False
        if len(stack) == 0:
            return True
        return False