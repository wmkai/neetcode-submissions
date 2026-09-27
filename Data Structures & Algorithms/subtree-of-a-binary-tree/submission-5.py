# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 标准面试解法是dfs，更高级解法是树序列化 + KMP / hashing，不需要掌握
        def is_same(p, q):
            if not p and not q:
                return True
            elif not p and q:
                return False
            elif p and not q:
                return False
            else:
                if p.val == q.val:
                    return is_same(p.left, q.left) and is_same(p.right, q.right)
                else:
                    return False

        def dfs(root, subRoot):
            if is_same(root, subRoot):
                return True
            else:
                if root.left:
                    return dfs(root.left, subRoot)
                if root.right:
                    return dfs(root.right, subRoot)
                return False
        return dfs(root, subRoot)