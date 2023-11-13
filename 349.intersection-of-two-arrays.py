#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst_ = []
        nums1_, nums2_ = list(set(nums1)), list(set(nums2))
        for _ in nums1_:
            if _ in nums2_:
                lst_.append(_)
        
        return lst_
        
        # @lc code=end

