class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        hash_table = {}

        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1

        for num, times in hash_table.items():
            freq[times].append(num)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for value in freq[i]:
                result.append(value)
                if len(result) == k:
                    return result