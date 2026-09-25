# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 本题和148.链表归并排序不一样，链表归并排序是两个无序链表合并成一个有序链表
        # 这样写更简洁
        dummy = ListNode()
        cur = dummy
        while list1 and list2: 
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        # 如果有一个链表没用完，就直接拼在后面     
        if list1 or list2:
            cur.next = list1 if list1 else list2            
        return dummy.next