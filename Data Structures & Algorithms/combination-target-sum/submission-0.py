class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(nums, ans):
            if sum(ans) == target:
                res.append(ans)
            if sum(ans) > target:
                return
            for i in range(len(nums)):
                dfs(nums[i:], ans + [nums[i]])
        dfs(nums, [])
        return res