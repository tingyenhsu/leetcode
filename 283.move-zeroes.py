#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if len(nums) <=1 or 0 not in nums:
        #     pass
        # else:
        #     while set(nums[nums.index(0):])!=set([0]):
        #         for ix, num in enumerate(nums):
        #             if ix != len(nums)-1:  #如果不是最後一筆
        #                 if nums[ix] == 0:
        #                     for _ in range(ix, len(nums)-1):
        #                         nums[_] = nums[_+1]
        #                     nums[-1] = 0
        # ---雙指針方法
        # x = 數值為0的index
        # 如果y的數值不為0, 則x, y的值互換
        # 如果y的數值為零, y的index +1
        # 大家都先從0開始
        x = 0
        y = 1
        while x <len(nums) and y <len(nums):
            if nums[x]==0 and nums[y] !=0:
                nums[x] = nums[y]
                nums[y] = 0
                x+=1
                y+=1
            elif nums[x]==0 and nums[y] ==0:
                y+=1
            else:
                x+=1
                y+=1
        
# @lc code=end

