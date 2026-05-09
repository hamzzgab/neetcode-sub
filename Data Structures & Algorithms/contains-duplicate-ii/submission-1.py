class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = set()

        for i, num in enumerate(nums):
            if (num in hash_map):
                return True
            hash_map.add(num)
            if len(hash_map) > k:
                hash_map.remove(nums[i-k])
        return False