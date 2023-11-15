#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # --- reference: https://leetcode.com/problems/linked-list-cycle/solutions/3999014/99-68-two-pointer-hash-table/
        # Floyd's Cycle-Finding Algorithm
        if head:
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                if slow == None or fast == None:
                    return 0
                elif slow == fast:
                    return 1
                else:
                    continue
        else:
            return 0


            

        
# @lc code=end

