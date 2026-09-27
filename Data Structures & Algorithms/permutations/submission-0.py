class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur_nums, ans):
            if len(ans) == len(nums):
                res.append(ans)
            for i in range(len(cur_nums)):
                dfs(cur_nums[:i] + cur_nums[i+1:], ans + [cur_nums[i]])
        dfs(nums, [])
        return res
        