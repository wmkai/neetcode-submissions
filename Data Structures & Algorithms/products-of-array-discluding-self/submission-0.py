class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
        right_prod = 1
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            right_prod = right_prod * nums[i+1]
            res[i] = res[i] * right_prod
        return res