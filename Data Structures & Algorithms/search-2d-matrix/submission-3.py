class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 思路：行二分+列二分，虽然思路简单，但很多细节容易出错，见代码注释
        # 注意：行二分和列二分时的mid下标容易写成同名的，这样是错的！
        m, n = len(matrix), len(matrix[0])
        u, d = 0, m-1 # u, d只用于行二分
        while u <= d:
            mid_row = u + (d - u) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][n-1]:
                l, r = 0, n-1 # l, r只用于列二分，应写在此处
                while l <= r:
                    mid_col = l + (r - l) // 2
                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif target < matrix[mid_row][mid_col]:
                        r = mid_col - 1
                    elif target > matrix[mid_row][mid_col]:
                        l = mid_col + 1
                return False # 重点：一旦该行内没找到，要退出，不然会死循环
            elif target < matrix[mid_row][0]:
                d = mid_row - 1
            elif target > matrix[mid_row][n-1]:
                u = mid_row + 1
        return False # 重点