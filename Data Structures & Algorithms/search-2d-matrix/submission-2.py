class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix) - 1 
        while u <= d:
            m = u + (d - u) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if matrix[m][mid] == target:
                        return True
                    elif matrix[m][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            elif target < matrix[m][0]:
                d = m - 1
            else:
                u = m + 1
        return False
