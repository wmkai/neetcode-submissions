class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        res = 0
        while i < j:
            cur = min(heights[i], heights[j]) * (j - i)
            res = max(res, cur)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return res
