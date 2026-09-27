# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def get_depth(root):
            if not root:
                return 0
            l_depth = get_depth(root.left)
            r_depth = get_depth(root.right)
            if abs(l_depth - r_depth) > 1:
                nonlocal is_balanced
                is_balanced = False
            return max(l_depth, r_depth) + 1
        get_depth(root)
        return is_balanced