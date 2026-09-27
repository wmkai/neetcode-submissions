# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 可以用DFS（后序遍历），也可以用层次遍历
        # DFS(首选)
        def dfs(root):
            if not root:
                return 0
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
        return dfs(root)

