# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_same(p, q):
            if p and not q:
                return False
            elif not p and q:
                return False
            elif not p and not q:
                return True
            else:
                if p.val == q.val:
                    return is_same(p.left, q.left) and is_same(p.right, q.right)
                else:
                    return False
        return is_same(p, q)