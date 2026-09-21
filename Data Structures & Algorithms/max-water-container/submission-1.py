class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            # 面积为min(h[i],h[j])×(j−i)，由短的那一边决定
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            # 在内收时，应该考虑内收哪个边有可能让面积增大
                # 1.内收短边可能导致面积增大，也可能减小
                # 2.而内收长边一定会导致面积减小,或不变
            # 因此，在内收i或j的时候，应该内收短边
            if height[l] < height[r]:  # 内收短边
                l += 1
            else:
                r -= 1
        return res


        