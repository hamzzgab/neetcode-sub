class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        _hash = {}

        for num in nums:
            _hash[num] = _hash.get(num, 0) + 1

        for key, val in _hash.items():
            if val % 2 != 0:
                return False

        return True
            