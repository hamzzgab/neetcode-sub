class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(matrix, len(matrix), len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True

        return False