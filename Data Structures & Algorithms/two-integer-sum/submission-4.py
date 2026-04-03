class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hash_set:
                return [hash_set[diff], idx]
            hash_set[num] = idx