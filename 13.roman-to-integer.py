#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        r_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s_lst = [r_dict[_] for _ in s]

        for i, item in enumerate(s_lst):
            if i+1 < len(s_lst):
                a = s_lst[i]
                b = s_lst[i+1]
                if a<b:
                    s_lst[i] = b-a
                    del s_lst[i+1]
                else:
                    pass
        return sum(_ for _ in s_lst)            

        
        
# @lc code=end

