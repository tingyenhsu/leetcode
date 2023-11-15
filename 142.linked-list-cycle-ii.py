#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # 遇到不等於起點
    # https://blog.csdn.net/Acx77/article/details/122725947
    # Floyd Cycle Detection Algorithm 的方法可以歸納為以下幾個步驟:
    # 使用快慢兩個指標 fast 和 slow。
    # 從頭結點開始,slow每次移動一個結點,fast每次移動兩個結點。
    # 查看fast和slow指標是否會相遇,有以下兩種情況:
    # (1) 如果fast遇到null,表示鏈表無迴圈。算法結束。
    # (2) 如果fast和slow相遇,表示鏈表有迴圈。轉到第4步。
    # 找到迴圈的入口結點:slow指標回到頭結點,fast指標留在相遇點不動。slow和fast每次移動一個結點,再次相遇時就是迴圈入口結點。
    # 返回迴圈入口結點。
    # 這個算法利用了快慢指標移動速度不同來判斷鏈表是否有迴圈,時間複雜度為 O(n),空間複雜度為 O(1)。
        if head:
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == None or fast == None:
                    return None
                elif slow == fast:   # [1,2] 兩個都會同時回到起點，這時候如果再走，就會return index=1的位置
                    if fast == head and slow == head:
                        return head
                    else:
                        slow = head
                        while fast and fast.next:
                            slow = slow.next
                            fast = fast.next
                            if slow == fast:
                                return slow
                            else:
                                continue
                else:
                    continue

        else:
            return None
# @lc code=end

