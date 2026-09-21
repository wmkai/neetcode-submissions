class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [[set() for j in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in row[i] and board[i][j] not in col[j]:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                else:
                    return False
                box_i, box_j = i // 3, j // 3
                if board[i][j] not in box[box_i][box_j]:
                    box[box_i][box_j].add(board[i][j])
                else:
                    return False
        return True              
                