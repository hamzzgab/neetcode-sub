class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [2, 20, 4, 10, 3, 4, 5] -> 4

        2  - 1 = 1 isThere No
        20 - 1 = 19 isThere No
        4  - 1 = 3 isThere yes 1
            3 - 1 isThere yes  2
            2 - 1 isThere yes  3
        10 - 1 = 9 isThere No
        5 - 1 = 4 isThere Yes     1
            4 - 1 = 3 isThere Yes 2
            3 - 1 = 2 isThere Yes 3

        """
        res = 0
        for num in nums:
            long = 0
            temp = num
            while temp in nums:                
                temp -= 1
                long += 1
            res = max(long, res)
        return res