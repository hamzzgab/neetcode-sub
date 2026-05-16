class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = {}

        for num in nums:
            hash[num] = 1 + hash.get(num, 0)
    
        return [key for key, val in hash.items() if val >= 2][0]