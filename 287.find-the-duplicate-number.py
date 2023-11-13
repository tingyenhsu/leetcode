#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict_ = dict.fromkeys(set(nums),0)
        for __ in [_ for _ in nums]:
            dict_[__] +=1
        return [key for key, value in dict_.items() if value >=2][0]
# @lc code=end

