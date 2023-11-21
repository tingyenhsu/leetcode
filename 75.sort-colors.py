#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            pass
        else:
            x = 0
            y = 1

            while x <= len(nums)-2:
                for y in range(x, len(nums)):
                    if nums[x] > nums[y]:
                        nums[x], nums[y] = nums[y], nums[x]
                x+=1
# @lc code=end

