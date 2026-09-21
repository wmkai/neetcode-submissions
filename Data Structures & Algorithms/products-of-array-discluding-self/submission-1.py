class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n)时间+O(1)空间的做法（重点：题目中说输出list不算额外空间）
        # 可以先用结果数组存i左边数的乘积，
        # 然后从左往右遍历，用一个临时变量存i右边数的乘积，然后乘到结果数组上
        # 总体思路和基础方法一样
        res = [1 for i in range(len(nums))] # 先用结果数组存i左边数的乘积
        for i in range(1, len(nums)): # 从左往右遍历
            res[i] = res[i-1] * nums[i-1]
        right_prod = 1 # 用一个临时变量存i右边数的乘积
        for i in range(len(nums)-2, -1, -1): # 从右往左遍历
            right_prod = right_prod * nums[i+1] # 更新right_prod
            res[i] = res[i] * right_prod # i左边的乘积 * i右边的乘积
        return res