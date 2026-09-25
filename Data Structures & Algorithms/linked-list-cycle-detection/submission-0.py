# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针相遇就说明有环，如果快指针到None就说明没有环，不需要dummy节点
        dummy = ListNode(next = head)
        fast, slow = dummy, dummy
        while fast and fast.next: # 注意：fast指针的判断条件不是fast.next and fast.next.next
            fast = fast.next.next
            slow = slow.next
            if fast == slow: # 慢指针追上了快指针说明有环
                return True
        return False # 快指针遇到None，说明没有环