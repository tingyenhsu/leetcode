#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i, item in enumerate(nums):
            if nums[i] == val:
                nums[i] = -1
            else:
                pass
        nums.sort(reverse=True)
        k = len([_ for _ in nums if _!=-1])
        return k

# @lc code=end

