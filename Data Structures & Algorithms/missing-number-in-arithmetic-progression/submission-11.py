class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        """
        1, 1, 1        
        0 / 3 = 0
        """

        diff = (arr[-1] - arr[0]) // len(arr)
        if diff == 0:
            return arr[0]
        for i in range(len(arr)-1):
            if arr[i] + diff not in arr:
                return arr[i] + diff
        return diff