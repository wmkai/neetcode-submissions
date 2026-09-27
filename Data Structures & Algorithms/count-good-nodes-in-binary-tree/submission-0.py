# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 如果从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值，那这个节点就是good node
        # 这题面试标准做法就是 DFS + 维护从根到当前节点路径上的最大值。
        res = 0
        def dfs(node, max_val):
            if not node:
                return
            if node.val >= max_val:
                nonlocal res
                res += 1
                max_val = max(max_val, node.val)
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, root.val)
        return res