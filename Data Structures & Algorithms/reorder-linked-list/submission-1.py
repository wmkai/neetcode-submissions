# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_list = [] # 用一个数组存节点（而不是数值），然后不断移动头尾双指针，进行链表重排序
        node = head
        while node:
            node_list.append(node)
            node = node.next
        l, r = 0, len(node_list) - 1 # 双指针
        while l < r:
            node_list[l].next = node_list[r]
            l += 1
            if l == r: # 偶数个节点的情况，会提前相遇
                break
            node_list[r].next = node_list[l]
            r -= 1
        node_list[l].next = None # 无论哪种情况，l都是最后一个节点