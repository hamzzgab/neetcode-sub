class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        _hash_set = set()

        for num in nums:
            if num not in _hash_set:
                _hash_set.add(num)
            else:
                _hash_set.remove(num)

        return not _hash_set
            