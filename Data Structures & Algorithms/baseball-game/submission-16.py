class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0
        for op in operations:
            if op == '+':
                a, b = record[-1], record[-2]
                total += a + b
                record.append(a + b)                
            elif op == 'C':
                value = record.pop() 
                total -= value
            elif op == 'D':
                new_score = 2 * record[-1]
                total += new_score
                record.append(new_score)
            else:
                total += int(op)
                record.append(int(op))
            print(record, total)
        return total