class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        for i in range(9):
            hash_set = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in hash_set:
                        return False
                    hash_set.add(board[i][j])

        for i in range(9):
            hash_set = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in hash_set:
                        return False
                    hash_set.add(board[j][i])
        
        for n in range(9):
            hash_set = set()
            for i in range(3):
                for j in range(3):
                    row = (n // 3) * 3 + i
                    col = (n % 3) * 3 + j
                    if board[row][col] != '.':
                        if board[row][col] in hash_set:
                            return False
                        hash_set.add(board[row][col])
            print(hash_set)

        return True