class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        hash = {}

        for i, num in enumerate(nums):
            hash[num] = hash.get(num, 0) + 1
        for num, times in hash.items():
            freq[times].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                if len(res) != k:
                    res.append(j)
                else:
                    break

        return res