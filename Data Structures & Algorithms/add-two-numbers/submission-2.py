# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        val, carry = 0, 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            val = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            node.next = ListNode(val = val, next = None)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry != 0:
            node.next = ListNode(val = carry, next = None)
        return dummy.next


        