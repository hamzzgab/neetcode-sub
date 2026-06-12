class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1] * len(arr)
        rightMax = -1
        for i in range(len(result) - 1, -1, -1):
            result[i] = rightMax
            rightMax = max(rightMax, arr[i])
        
        return result