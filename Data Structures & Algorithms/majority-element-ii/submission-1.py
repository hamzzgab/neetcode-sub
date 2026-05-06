from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        5, 2, 3, 2, 2, 2, 2, 5, 5, 5
        -------
        10 // 3 = 3

        nums | count
        2    | 4
        5    | 3        
        """

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            
            if len(count) <= 2:
                continue

            new_count = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    new_count[num] = c - 1
            count = new_count             

        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)           
        
        return res
