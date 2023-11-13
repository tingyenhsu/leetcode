#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # def check_english(c):
        #     ascii_value = ord(c)
        #     return (ascii_value >= 65 and ascii_value <= 90) or (ascii_value >= 97 and ascii_value <= 122)
        # s2 = [_ for _ in s]
        # x = 0
        # y = -1
        # while x +(-y)<=len(s2)-1:
        #     if check_english(s2[x]) and check_english(s2[y]):
        #         s2[x], s2[y] = s2[y], s2[x]
        #         x+=1
        #         y+=-1
        #     elif check_english(s2[x]) and not check_english(s2[y]):
        #         y+=-1
        #     elif not check_english(s2[x]) and check_english(s2[y]):
        #         x+=1
        #     else:
        #         x+=1
        #         y+=-1
        # return ''.join(s2)
        s2 = [_ for _ in s]
        x = 0
        y = -1
        while x +(-y)<=len(s2)-1:
            if s2[x].isalpha() and s2[y].isalpha():
                s2[x], s2[y] = s2[y], s2[x]
                x+=1
                y+=-1
            elif s2[x].isalpha() and not s2[y].isalpha():
                y+=-1
            elif not s2[x].isalpha() and s2[y].isalpha():
                x+=1
            else:
                x+=1
                y+=-1
        return ''.join(s2)
# @lc code=end

