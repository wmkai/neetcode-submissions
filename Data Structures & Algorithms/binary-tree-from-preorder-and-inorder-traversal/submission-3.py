# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder 用来确定根节点，inorder 用来划分左右子树

        # 记录每个值在 inorder 中的位置，避免每次 inorder.index()
        index = {val: i for i, val in enumerate(inorder)}

        pre_idx = 0

        def dfs(left, right):
            nonlocal pre_idx

            if left > right:
                return None

            # preorder 当前节点就是当前子树的根
            num = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(num)

            # 根节点在 inorder 中的位置
            idx = index[num]

            # idx 左边属于左子树，右边属于右子树
            root.left = dfs(left, idx - 1)
            root.right = dfs(idx + 1, right)

            return root

        return dfs(0, len(inorder) - 1)