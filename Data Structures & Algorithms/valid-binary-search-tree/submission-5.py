# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 二叉搜索树中序遍历是有序数组
        nums = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        dfs(root)
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]: # 元素不能相等
                return False
        return True