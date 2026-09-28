class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        matrix = [['.' for j in range(n)] for i in range(n)]
        def is_valid(row, col): 
        # 由于对不同行递归，所以这里只需要检查列和斜线上是否重叠
            # 检查该列上是否有元素
            r = row - 1
            while r >= 0:
                if matrix[r][col] == 'Q':
                    return False
                r -= 1
            # 检查斜率为1的线上是否有重叠，由于递归行是从小到大，因此只要检查比row小的行
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if matrix[r][c] == 'Q':
                    return False
                r -= 1
                c += 1
            # 检查斜率为-1的线上是否有重叠，由于递归行是从小到大，因此只要检查比row小的行
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if matrix[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            return True

        def dfs(row):
            if row == n:
                ans = []
                for i in range(n):
                    ans.append(''.join(matrix[i])) # 把矩阵按行转为str加入list
                res.append(ans)
                return
            for col in range(n):
                if is_valid(row, col):
                    matrix[row][col] = 'Q'
                    dfs(row + 1)
                    matrix[row][col] = '.' # 记得复原
        dfs(0)
        return res
        