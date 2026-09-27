# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if p and not q:
                return False
            elif not p and q:
                return False
            elif not p and not q:
                return True
            else:
                if p.val == q.val:
                    return dfs(p.left, q.left) and dfs(p.right, q.right)
                else:
                    return False
        return dfs(p, q)