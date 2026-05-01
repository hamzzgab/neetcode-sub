class Solution:
    def majorityElement(self, nums: List[int]) -> int:        
        hash = {}
        counter = len(nums) // 2
        for num in nums:
            hash[num] = hash.get(num, 0) + 1

        return [val for val, times in hash.items() if times > counter][0]

        