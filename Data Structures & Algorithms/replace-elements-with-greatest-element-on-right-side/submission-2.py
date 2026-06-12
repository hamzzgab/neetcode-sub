class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1] * len(arr)
        infix = -1
        temp = -1
        for i in range(len(result) - 1, -1, -1):
            result[i] = max(infix, temp)
            infix = arr[i]
            temp = result[i]
        
        return result