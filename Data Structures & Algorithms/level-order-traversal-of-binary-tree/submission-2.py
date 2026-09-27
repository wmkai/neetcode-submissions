class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 层序遍历
        queue = []
        if not root:
            return []
        res = []
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)): # 通过这个判断层次遍历在哪一层
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res