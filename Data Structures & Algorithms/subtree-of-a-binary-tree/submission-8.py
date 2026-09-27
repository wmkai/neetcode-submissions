# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:
        # 标准面试解法：DFS 遍历 root 的每个节点，
        # 在每个节点处判断该子树是否和 subRoot 完全相同
        # 更高级解法：树序列化 + KMP / hashing，一般不需要掌握

        def is_same(p, q):
            # 两棵树都为空，说明当前部分相同
            if not p and not q:
                return True

            # 只有一棵为空，结构不同
            elif not p and q:
                return False

            elif p and not q:
                return False

            else:
                # 当前节点值相同后，还需要左右子树都相同
                if p.val == q.val:
                    return (
                        is_same(p.left, q.left)
                        and is_same(p.right, q.right)
                    )
                else:
                    return False

        def dfs(root):
            # 已经遍历到空节点，说明这条路径没找到
            if not root:
                return False

            # 尝试把当前 root 当作 subRoot 的根
            if is_same(root, subRoot):
                return True
            else:
                # 当前节点不匹配，则继续去左右子树寻找
                return dfs(root.left) or dfs(root.right)

        return dfs(root)