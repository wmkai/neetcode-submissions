class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        def is_valid(i, j, idx):
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[idx] and not visited[i][j]:
                return True
            return False

        def dfs(i, j, idx):
            if idx == len(word) - 1:
                return True
            for dire in directions:
                next_i = i + dire[0]
                next_j = j + dire[1]
                if is_valid(next_i, next_j, idx + 1):
                    visited[next_i][next_j] = 1
                    if dfs(next_i, next_j, idx + 1):
                        return True
                    visited[next_i][next_j] = 0
            return False

        for i in range(m):
            for j in range(n):
                if is_valid(i, j, 0):
                    visited[i][j] = True
                    if dfs(i, j, 0):
                        return True
                    visited[i][j] = False
        return False
        