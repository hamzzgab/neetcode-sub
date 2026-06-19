class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = (arr[-1] - arr[0]) // len(arr)        
        expected = arr[0]
        for i in range(len(arr)-1):
            if arr[i] != expected:
                return expected
            expected += diff
        return expected