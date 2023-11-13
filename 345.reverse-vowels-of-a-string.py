#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        x=0   # 遇到母音停下來
        y=-1  # 從後面開始，遇到母音停下來
        s2 = [_ for _ in s]
        vowels = ['a','e','i','o','u']
        while x + (-y) <= len(s2):
            if s2[x].lower() in vowels and s2[y].lower() in vowels:
                s2[x], s2[y] = s2[y], s2[x]
                x+=1
                y+=-1
            elif s2[x].lower() in vowels and s2[y].lower() not in vowels:
                y+=-1
            elif s2[x].lower() not in vowels and s2[y].lower() in vowels:
                x+=1
            else:
                x+=1
                y+=-1
        return ''.join(s2)
        
# @lc code=end

