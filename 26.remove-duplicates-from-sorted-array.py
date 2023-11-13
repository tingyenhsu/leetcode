#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        y = 1
        while y <= len(nums)-1:
            if nums[y]=='_':
                break
            elif nums[x] == nums[y]:
                nums.pop(nums.index(nums[x]))
                # nums.append('_')
            else:
                x+=1
                y+=1
        # return len([_ for _ in nums if _!='_'])
        return len(nums)
# @lc code=end

