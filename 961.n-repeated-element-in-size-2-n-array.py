#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)/2
        x = 0
        temp = []
        counter = 0
        while x < len(nums)-1:
            if nums[x] not in temp:
                temp.append(nums[x])
                counter +=1
                for y in range(x+1, len(nums)):
                    if nums[y] == nums[x]:
                        counter +=1
                        if counter == n:
                            return nums[x]
            else:
                counter = 0
                x+=1
# @lc code=end

