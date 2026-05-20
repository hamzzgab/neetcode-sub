class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        score = 0
        for op in operations:
            if op == "C":
                val = stack.pop()
                score -= val
            elif op == "D":
                temp = stack[-1] * 2
                score += temp
                stack.append(temp)
            elif op == "+":
                temp = stack[-2] + stack[-1]
                score += temp
                stack.append(temp)
            else:
                score += int(op)
                stack.append(int(op))

        return score
