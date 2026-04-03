class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue

            target = -1 * num
            l, r = index + 1, len(nums) - 1

            while l < r:
                two_sum = nums[l] + nums[r]

                if two_sum < target:
                    l += 1
                elif two_sum > target:
                    r -= 1
                else:
                    three_sum = [nums[index], nums[l], nums[r]]
                    res.append(three_sum)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res