# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 题意：有两个链表，每个节点都放一位数（左边是低位，右边是高位），求两个链表的数相加后的结果，放在一个新链表中
        # 注意：要考虑进位
        dummy = ListNode(0) # 输出链表的头节点
        cur = dummy # 用来遍历构造输出链表的节点
        carry = 0
        # 这题一定要用or来判断，用and判断会很麻烦！
        while l1 or l2:  # 每当符合判断条件，就新增一个节点
        # 当一个链表遍历完，而另一个没遍历完时，用0补上缺的节点
        # 全部遍历完，但进位没处理完的时候，还要新建一个节点
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            sum_val = digit1 + digit2 + carry
            digit = sum_val % 10
            carry = sum_val // 10
            cur.next = ListNode(val = digit)
            cur = cur.next
            if l1: # 如果l1没遍历完，就更新指针
                l1 = l1.next
            if l2: # 如果l2没遍历完，就更新指针
                l2 = l2.next
        if carry != 0:
            cur.next = ListNode(val = carry)
        return dummy.next