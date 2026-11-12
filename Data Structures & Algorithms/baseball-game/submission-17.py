class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0
        for op in operations:
            if op == '+':
                a, b = record[-1], record[-2]
                _sum = a + b
                total += _sum
                record.append(_sum)                
            elif op == 'C':
                total -= record.pop() 
            elif op == 'D':
                _mult = 2 * record[-1]
                total += _mult
                record.append(_mult)
            else:
                total += int(op)
                record.append(int(op))
        return total