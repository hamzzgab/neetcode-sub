class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash = {}

        for num in nums:
            hash[num] = hash.get(num, 0) + 1

        return [num for num, times in hash.items() if times > len(nums) // 3]