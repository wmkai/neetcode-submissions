# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 题意：求一条最大的路径和（路径可能不经过root）
        # 思路：这题和543.二叉树的直径很像，都是求一条路径，路径可能不经过root，
        # 做法也类似，dfs过程中，对于每一个节点，都把他看做root，求以它为中心时，左右子树最大的路径和。dfs每个节点的过程中，我们需要用一个变量，取所有节点路径和的最大值。
        
        res = -float('inf') # 初始化为最小值
        
        def dfs(node): # 返回这个节点作为左子树或右子树时，能带来的最大路径和
            if not node:
                return 0 # 没有节点，和为 0
            # 重点：子树是负数时，直接丢弃
            l_sum = max(0, dfs(node.left)) # 左子树最大链和
            r_sum = max(0, dfs(node.right)) # 右子树最大链和
            nonlocal res
            res = max(res, node.val + l_sum + r_sum) # 注意：计算时，左右孩子都要带上
            # 由于之前l_sum和r_sum已经和0取过max，因此子树是负值时，会自动被舍弃
            return node.val + max(l_sum, r_sum) # 注意：返回时，只能带上他的一个最大的孩子
        dfs(root)
        return res