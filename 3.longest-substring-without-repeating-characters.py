#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = 0  # 慢指針
        y = 1  # 下一個遇到s[x]的位置

        length = 0

        if len(s) == 1:
            length = 1
        else:
            while y <= len(s)-1:
                if s[y] not in s[x:y] and y+1 <=len(s)-1:
                    y+=1
                else:
                    # 如果等於的話或遇到尾巴的話
                    if y == len(s)-1:
                        if s[y] in s[x:y]:
                            if len(s[x:y]) > length:
                                length = len(s[x:y])
                        else:
                            if len(s[x:]) > length:
                                length = len(s[x:])
                        break
                    elif len(s[x:y]) > length:
                        length = len(s[x:y]) 
                        x += 1
                        y = x+1
                    else:
                        x += 1
                        y = x+1
                        
        return length
                    
# @lc code=end

