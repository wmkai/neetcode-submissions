# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 这题面试里的标准做法是直接利用 BST 的性质，不需要像普通二叉树 LCA 那样做复杂 DFS。
        def dfs(node):
            # p 和 q 都比当前节点小，说明都在node的左子树
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            # p 和 q 都比当前节点大，说明都在node的右子树
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right)
            # 否则说明：
            # 1. p 和 q 分别在当前节点两侧，或者
            # 2. 当前节点本身就是 p 或 q
            # 因此当前节点就是最低公共祖先
            else:
                return node

        return dfs(root)