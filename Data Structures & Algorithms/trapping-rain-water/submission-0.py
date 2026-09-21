class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]
        for i in range(1, len(height)):
            left[i] = max(height[i-1], left[i-1])
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(height[i+1], right[i+1])
        for i in range(len(height)):
            if min(left[i], right[i]) > height[i]:
                res += min(left[i], right[i]) - height[i]
        return res