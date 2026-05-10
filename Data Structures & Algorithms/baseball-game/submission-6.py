class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        top = 0
        for i, op in enumerate(operations):            
            if op == '+':                
                a, b = stack[top - 1], stack[top - 2]
                stack.append(a + b)
                top += 1
            elif op == 'C':
                stack.pop()
                top -= 1
            elif op == 'D':
                stack.append(stack[-1] * 2)
                top += 1
            else:
                stack.append(int(op))            
                top += 1
        _sum = 0
        for val in stack:
            _sum += val
        return _sum