# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 前后序or层次遍历都可以
        # 中序不行，因为先左孩子交换孩子，再根交换孩子（做完后，右孩子已经变成了原来的左孩子），再右孩子交换孩子（此时其实是对原来的左孩子做交换）
        # 只要把每一个节点的左右孩子翻转一下的遍历方式都是可以的

        # 后序遍历
        def invert(node):
            if not node:
                return None
            node.left = invert(node.left)
            node.right = invert(node.right)
            node.left, node.right = node.right, node.left
            return node
        return invert(root)

        # 层次遍历
        # if not root:
        #     return None
        # queue = []
        # queue.append(root)
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.pop(0)
        #         node.left, node.right = node.right, node.left
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return root