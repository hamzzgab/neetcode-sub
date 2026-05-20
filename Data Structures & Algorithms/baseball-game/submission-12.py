class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        score = 0
        for op in operations:
            print(stack, end = ' | ')
            if op == 'C':                
                val = stack.pop()
                score -= val
                print(f'C: {stack}')
            elif op == 'D':
                temp = stack[-1] * 2
                score += temp
                stack.append(temp)
                print(f'D: {stack}')
            elif op == '+':
                temp = stack[len(stack) - 2] + stack[-1]
                score += temp
                stack.append(temp)
                print(f'+: {stack}')
            else:
                score += int(op)
                stack.append(int(op))            
                print(f'A: {stack}')

        return score