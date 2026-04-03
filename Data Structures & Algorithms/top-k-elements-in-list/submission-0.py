class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for _ in range(len(nums) + 1)]
        hash = {}
        for num in set(nums):
            hash[num] = nums.count(num)

        for key, val in hash.items():
            frequency[val].append(key)
        
        result = []
        for freq in frequency[::-1]:
            for val in freq:                
                result.append(val)
                if len(result) == k:
                    return result                