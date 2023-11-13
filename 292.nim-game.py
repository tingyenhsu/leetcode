#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        # 當n為4的倍數的時候，敵方一定會贏(因為我最多也只能拿3顆)
        return False if n%4==0 else True
        
# @lc code=end

