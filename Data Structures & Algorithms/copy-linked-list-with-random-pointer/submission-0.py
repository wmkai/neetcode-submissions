"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 题意：深拷贝一个链表，每个节点有两个指针(next和random)，是133的链表版本
        # 思路：做法和133基本一样，可以用DFS/BFS，但DFS更好理解，因此只提供DFS解法
        # 用一个visted字典存 旧节点 -> 新节点
        visited = {} 
        def dfs(node):
            if not node:
                return None
            if node in visited: # 注意：节点已经在dict中的情况下，也要返回新节点
                return visited[node]
            # 接下来的情况是节点不在dict中的情况，需要根据值new一个，并dfs孩子节点
            clone_node = Node(node.val, None, None) # 生成新节点
            visited[node] = clone_node # 在visited标记新节点
            clone_node.next = dfs(node.next) # 更新clone_node.next
            clone_node.random = dfs(node.random) # 更新clone_node.random
            return clone_node # 最后记得返回新生成的节点
        return dfs(head)