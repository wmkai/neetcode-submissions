# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 题意：给定一个链表，删除倒数第n个节点
        # 思路：快慢指针，快指针先走N步。然后和慢指针一起走，快指针走到链表最后一个节点的时候，慢指针正好在倒数第n个节点的前一个节点。
        # 如果用while fast判断的话，慢指针正好会走到倒数第n个节点。要想让慢指针在前一个节点（便于删除后面这个节点），要用while fast.next判断。
        # 因为可能被删除的是头结点，所以要加入dummy节点。
        dummy = ListNode(next = head)
        fast, slow = dummy, dummy
        for i in range(n):
            fast = fast.next
        while fast.next: # 用fast.next判断，跳出循环的时候，慢指针正好在'要删除节点'的前一位
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next # 删除slow后一个节点
        return dummy.next