class Solution:
    def trap(self, height: List[int]) -> int:
        # 思路：对每一列，寻找两侧高度最大的列，max_left和max_right，取较小的一个。
        # 这一列的雨水量就是1 * (min(left_max, right_max) - height)(当左右两边有比它高的柱子时，否则无法积水)
        # 计算每一列的left_max[i]和right_max[i]的过程会涉及到很多重复计算，复杂度是0(n^2)，因此用dp来做，O(n)。
        left_max = [0 for i in range(len(height))]
        right_max = [0 for i in range(len(height))]
        # 从左到右遍历，得到每个left_max[i]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])
        # 从右到左遍历，得到每个right_max[i]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
        # 计算每一列的雨水量
        res = 0
        for i in range(len(height)):
            if min(left_max[i], right_max[i]) > height[i]:
                res += 1 * (min(left_max[i], right_max[i]) - height[i]) # 注意：要减去当前列自身的高度
        return res