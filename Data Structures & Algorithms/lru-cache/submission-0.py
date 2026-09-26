# 题意：实现LRU缓存
# 思路：用双向链表+哈希表实现，头尾分别一个dummy节点。

# 创建双向链表
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # 构建首尾节点, 使之相连，这两个都是dummy节点
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.lookup = dict() # lookup作用是根据key找node
        self.max_len = capacity # 允许的最多节点数

    # 需要自己新增的两个函数：
    # 1. 删除链表节点
    def remove(self, node):
        del self.lookup[node.key] # 在lookup中删除节点
        node.prev.next = node.next # 修改节点前后指针关系
        node.next.prev = node.prev
        
    # 2. 在链表尾添加节点
    def add(self, node):
        self.lookup[node.key] = node # 在lookup中添加节点
        prev_tail = self.tail.prev # 修改节点前后指针关系
        node.next = self.tail
        self.tail.prev = node
        prev_tail.next = node
        node.prev = prev_tail

    def get(self, key: int) -> int:
        if key in self.lookup: # 如果node存在
            node = self.lookup[key]
            self.remove(node) # 就先删掉
            self.add(node) # 再添加同样的节点，目的是让这个节点去链表尾部
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 有两种情况需要先删除节点：
        if key in self.lookup: # 1.如果key对应的node存在，就删掉旧节点
            self.remove(self.lookup[key])
        elif len(self.lookup) == self.max_len: # 2.如果数量超了，就删掉最不常用的节点
            # 把表头位置节点删除(最不常用的数据值)
            self.remove(self.head.next)
        self.add(Node(key, value)) # 删好后，添加节点
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)