class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        hash_set = {}

        for num in nums:
            hash_set[num] = hash_set.get(num, 0) + 1

        print(hash_set)

        for value, count in hash_set.items():
            freq[count].append(value)
            print(freq)

        res = []
        for idx in range(len(freq) - 1, -1, -1):
            for value in freq[idx]: 
                res.append(value)
                if len(res) == k:                    
                    return res                