#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head and k !=0:
            # get the length
            length = 1
            x = head
            while x.next:
                x = x.next
                length += 1
            count = length - (k % length)  # 往回走幾步
            if length == 1 or count ==0:
                return head
            else:
                # connect to the head 
                x.next = head 
                # back to the head
                y = x
                while count >0:
                    y = y.next
                    count += -1
                new_head = y.next
                y.next = None
                return new_head

        else:
            return head

# @lc code=end

