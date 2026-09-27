# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 题意：找二叉树的直径，直径是任意两个节点之间的最长距离（可能不经过root）
        # 思路：dfs过程中，对于每一个节点，都把他看做root，求以它为中心时，左右子树的高度和，这就是这个节点的直径。dfs每个节点的过程中，我们需要用一个变量，取所有节点直径的最大值。
        res = 0
        
        def get_depth(node):
            if not node:
                return 0
            l_depth = get_depth(node.left)
            r_depth = get_depth(node.right)
            nonlocal res
            res = max(res, l_depth + r_depth) # 去掉这一行的话就是求二叉树高度
            return max(l_depth, r_depth) + 1
        
        get_depth(root)
        return res