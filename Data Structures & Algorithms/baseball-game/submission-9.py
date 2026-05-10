class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, res = [], 0
        for i, op in enumerate(operations):
            if op == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                res -= stack.pop()
            elif op == "D":
                res += stack[-1] * 2
                stack.append(stack[-1] * 2)
            else:
                res += int(op)
                stack.append(int(op))
        return res
