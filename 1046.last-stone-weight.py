#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>=2:
            y = max(stones)
            y_ = stones.index(y)
            stones.pop(y_)
            x = max(stones)
            x_ = stones.index(x)
            stones.pop(x_)
            z = y-x
            if z==0:
                pass
            else:
                stones.append(z)
        return stones[0] if len(stones)>=1 else 0
# @lc code=end

