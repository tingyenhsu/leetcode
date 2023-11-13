#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        x = 0
        y = -1
        while x != round(len(s)/2):
            s[x], s[y] = s[y], s[x]
            x+=1
            y+=-1
        
# @lc code=end

