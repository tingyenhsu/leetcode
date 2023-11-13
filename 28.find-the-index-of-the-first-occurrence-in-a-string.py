#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        y = 0
        found = 0
        if haystack == needle:
            found = 1
            return 0
        else:
            while y <= len(haystack)-1:
                if haystack[y:y+len(needle)] == needle:
                    found = 1
                    return y
                else:
                    y+= 1
        if found ==0:
            return -1
        
# @lc code=end

