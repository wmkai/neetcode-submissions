class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 思路：用多个set，判断行、列、块中，是否存在重复元素
        # 3x3 sub-boxes 由粗实线划分
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [[set() for j in range(3)] for i in range(3)] # 用二维数组比较方便
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': # 空白首先跳过
                    continue
                # row
                if board[i][j] in row[i]:
                    return False
                else:
                    row[i].add(board[i][j])
                # col
                if board[i][j] in col[j]:
                    return False                
                else:
                    col[j].add(board[i][j])
                # box
                box_i, box_j = i // 3, j // 3
                if board[i][j] not in box[box_i][box_j]:
                    box[box_i][box_j].add(board[i][j])
                else:
                    return False
        return True
        