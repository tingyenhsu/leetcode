#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst_ = []
        if len(nums1) > len(nums2):
            min_lst = nums2
            max_lst = nums1
        else:
            min_lst = nums1
            max_lst = nums2
                
        for _ in min_lst:
            if _ in max_lst:
                ix = max_lst.index(_)
                lst_.append(max_lst.pop(ix))
        return lst_
# @lc code=end

