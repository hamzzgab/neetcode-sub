from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Horizontal check
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[row])):
                if board[row][col] != '.':
                    val = board[row][col]
                    if val in seen:
                        return False
                    seen.add(val)

        # Vertical check
        for col in range(len(board)):
            seen = set()
            for row in range(len(board[col])):
                if board[row][col] != '.':
                    val = board[row][col]
                    if val in seen:
                        return False
                    seen.add(val)
                
        # Grid check
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    box_key = (r//3, c//3)
                    if val in boxes[box_key]:
                        return False
                    boxes[box_key].add(val)

        return True