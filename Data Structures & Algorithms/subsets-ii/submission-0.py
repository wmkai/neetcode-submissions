class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(cur_nums, ans):
            res.append(ans)
            for i in range(len(cur_nums)):
                if i > 0 and cur_nums[i] == cur_nums[i-1]:
                    continue
                dfs(cur_nums[i+1:], ans + [cur_nums[i]])
        dfs(nums, [])
        return res
        