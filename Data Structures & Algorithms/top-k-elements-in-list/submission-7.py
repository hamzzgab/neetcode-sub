class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        repetitions = {}

        for num in nums:
            repetitions[num] = repetitions.get(num, 0) + 1

        for num, times in repetitions.items():
            freq[times].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res                

        return res