class Solution:
    def majorityElement(self, nums: List[int]) -> int:        
        m = None
        c = 0
        for num in nums:
            if c == 0:
                m = num
                c = 1
            elif m == num:
                c += 1
            else:
                c -= 1
        return m