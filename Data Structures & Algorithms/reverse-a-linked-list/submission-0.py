class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 反转链表不用dummy节点，需要一个pre=None，一个cur，一个next。
        if not head:
            return None
        pre, cur = None, head # 这个pre = None是最重要的
        while cur:
            # 不要用多元赋值，多元赋值顺序会影响结果
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre