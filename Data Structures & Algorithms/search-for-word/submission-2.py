class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 这题需要回溯，因此不能使用BFS，只能用DFS
        m, n = len(board), len(board[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def is_valid(i, j, idx): # 检查是否越界、是否访问过、单词是否合规
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[idx] and not visited[i][j]:
                return True
            return False
        def dfs(i, j, cur_idx):
            if cur_idx == len(word) - 1: # 由于在进入dfs函数前，已经判断了该字符是否合规，因此当idx到达目标单词长度时，就表示找到解了
                return True
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if is_valid(next_i, next_j, cur_idx + 1):
                    visited[next_i][next_j] = 1
                    if dfs(next_i, next_j, cur_idx + 1): # 每层dfs需要接受下一层传上来的结果，如果有一个True，需要一直传递上去
                        return True
                    visited[next_i][next_j] = 0 # 重点：由于本题需要回溯，因此dfs出来后，要重新把状态为清零
            return False

        for i in range(m):
            for j in range(n):
                if is_valid(i, j, 0):
                    visited[i][j] = True
                    if dfs(i, j, 0):
                        return True
                    visited[i][j] = False
        return False