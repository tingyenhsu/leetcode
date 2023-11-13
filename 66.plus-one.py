#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_lst = []
        for _ in str(int(''.join(str(_) for _ in digits))+1):
            new_lst.append(int(_))
        return new_lst
        
# @lc code=end

