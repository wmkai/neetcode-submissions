class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 题意：满足组合的sum为target，注意：元素可以重复使用   
        # 可以用DFS回溯(首选)，也可以看做是背包问题，用dp解

        # 1.使用新数组当递归参数(首选)
        res = []
        nums.sort()
        def dfs(nums, ans):
            if sum(ans) == target: # 因为数组中都是正数，所以找到一组结果，说明到了叶子节点
                res.append(ans)
                return
            for i in range(len(nums)):
                if sum(ans) > target: # 剪枝，当前结果已经大于target，而且数组中全是正数，再往后只会让结果更大
                    break
                # 元素可能重复使用，且原素组没有重复元素
                dfs(nums[i:], ans + [nums[i]]) 
        dfs(nums, [])
        return res

        # 2.使用索引