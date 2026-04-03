class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            l, r = 0, len(matrix[i]) - 1
            while l <= r:                
                m = l + ((r - l) // 2)
                print(f'In the matrix {matrix[i]}\n{l},{matrix[i][m]},{r}')
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] < target:
                    l = m + 1
                else:
                    r = m - 1
            i += 1
        return False