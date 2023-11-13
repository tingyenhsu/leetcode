#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_lst = s.strip(' ').split(' ')
        return len(word_lst[-1])
        
# @lc code=end

