class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _hash = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in _hash:
                return [_hash[diff], i]

            _hash[num] = i