#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        n_ = bin(n)[2:]
        x = 0 # index of first 1
        y = 1 # search for second 1
        distance = 0
        
        while y <= len(n_)-1:
            if n_[y]!='1':
                y+=1
            elif n_[y]=='1':
                if y-x > distance:
                    distance = y-x
                else:
                    x=y
                    y+=1
            else:
                y+=1
                
        return distance
        
# @lc code=end

