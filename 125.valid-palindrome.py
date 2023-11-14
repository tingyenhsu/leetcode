#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s2 = ''.join(x.lower() for x in s if x.isalpha()|x.isdigit())
        # x = 0
        # y = -1
        # flag = 1
        # while x < round(len(s2)/2):
        #     if s2[x] == s2[y]:
        #         x+=1
        #         y+=-1
        #     else:
        #         flag = 0
        #         break
        # return flag

        # 運用 isalnum
        s2 = ''.join(x.lower() for x in s if x.isalnum())
        return True if s2==s2[::-1] else False

    
# @lc code=end

