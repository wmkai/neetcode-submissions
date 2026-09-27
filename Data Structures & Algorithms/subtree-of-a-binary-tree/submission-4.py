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

        is_subtree = False
        def dfs(root, subRoot):
            nonlocal is_subtree
            if is_same(root, subRoot):
                is_subtree = True
            else:
                if root.left:
                    dfs(root.left, subRoot)
                if root.right:
                    dfs(root.right, subRoot)
            # nonlocal is_subtree
            # if not subRoot:
            #     return True
            # elif not root and subRoot:
            #     return False
            # elif is_same(root, subRoot):
            #     is_subtree = True
            #     return True
            # else:
            #     return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        dfs(root, subRoot)
        return is_subtree