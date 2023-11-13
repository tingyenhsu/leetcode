#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x_ = 0
        while x_ <= (len(numbers)-1):
            y = target-numbers[x_]
            if y in numbers[x_+1:]:
                y_ = numbers[x_+1:].index(y)+x_+1
                break
            x_+=1
        
        return [x_+1, y_+1]
# @lc code=end

