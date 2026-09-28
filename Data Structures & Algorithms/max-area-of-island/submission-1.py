class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def is_valid(x, y): # 检查是否越界、是否访问过、是否为地面
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and visited[x][y] == 0:
                return True
            else:
                return False

        # dfs解法 代码量更少
        def dfs(x, y):
            visited[x][y] = 1
            for direction in directions:
                next_x = x + direction[0]
                next_y = y + direction[1]
                if is_valid(next_x, next_y):
                    dfs(next_x, next_y)
                    # 可以写在几个不同的位置，只要保证访问节点的时候有就好
                    # visited[next_x][next_y] = 1 
                    
        res = 0
        for i in range(m):
            for j in range(n):
                if is_valid(i, j):
                    dfs(i, j)
                    res += 1
        return res    

        # bfs解法
        # def bfs(x, y):
        #     queue = []
        #     visited[x][y] = 1 # BFS visited数组必须在入队时置1，如果等到出队时置1，会导致有一个节点多次入队。
        #     queue.append((x, y)) 
        #     while queue:
        #         for i in range(len(queue)):
        #             x, y = queue.pop(0)
        #             for direction in directions:
        #                 next_x = x + direction[0]
        #                 next_y = y + direction[1]
        #                 if is_valid(next_x, next_y):
        #                     visited[next_x][next_y] = 1 # BFS visited数组必须在入队时置1，如果等到出队时置1，会导致有一个节点多次入队。
        #                     queue.append((next_x, next_y))
        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if is_valid(i, j):
        #             bfs(i, j)
        #             res += 1
        # return res
        
        