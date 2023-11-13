#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for _ in s:
            if _ in ['(','[','{']:
                stack.append(_)
            else:
                if not stack \
                    or (_ == ')' and stack[-1] != '(' )\
                    or (_ == ']' and stack[-1]!='[')\
                    or (_ == '}' and stack[-1]!='{'):
                        return False
                stack.pop()
        return not stack  # 檢查stack是否為空

# @lc code=end

