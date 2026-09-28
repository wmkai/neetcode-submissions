class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 0

        def is_valid(x, y):
            if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] == '1':
                return True
            return False
        
        def dfs(x, y):
            visited[x][y] = 1
            for dire in directions:
                next_x = x + dire[0]
                next_y = y + dire[1]
                if is_valid(next_x, next_y):
                    dfs(next_x, next_y)

        
        for i in range(m):
            for j in range(n):
                if is_valid(i, j):
                    dfs(i, j)
                    res += 1
        return res