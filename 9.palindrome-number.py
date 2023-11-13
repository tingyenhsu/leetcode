#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        for _ in str(x):
            stack.append(_)
        for _ in str(x):
            if _ != stack.pop():
                return False
        return True
    
        # str_x = str(x)
        # if len(str(x))==1:
        #     return True
        # else:
        #     if len(str_x)%2 !=0:
        #         index_ = round((len(str_x)-1)/2)  
        #         b = str_x[index_+1:]  
        #     else:
        #         index_ = round(len(str_x)/2)
        #         b = str_x[index_:]
        #     a = str_x[:index_]
        #     return a == b[::-1]

# @lc code=end

