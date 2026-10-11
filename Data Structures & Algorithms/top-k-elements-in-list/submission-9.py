class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        hash_map = {}

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        for num, times in hash_map.items():
            freq[times].append(num)

        result = []
        for times in range(len(freq) - 1, -1, -1):
            for num in freq[times]:
                result.append(num)
                if len(result) == k:
                    return result                