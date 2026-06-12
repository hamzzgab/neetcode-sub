class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0
        for op in operations:
            if op == '+':
                a, b = stack[-1], stack[-2]                
                result += (a + b)
                stack.append(a + b)
            elif op == 'D':
                result += (stack[-1] * 2)
                stack.append(stack[-1] * 2)
            elif op == 'C':
                result -= stack[-1]
                stack.pop()
            else:
                result += int(op)
                stack.append(int(op))
        return result