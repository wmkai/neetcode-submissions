class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 子集问题和组合问题的不同是：子集的每一条路径都要加入结果中(路径不一定要到叶子节点)
        def dfs(cur_nums, ans):
            res.append(ans) # 这里会自动加入空集，要放在终止添加的上面，否则会漏掉自己           
            for i in range(len(cur_nums)):
                dfs(cur_nums[i+1:], ans + [cur_nums[i]])
        dfs(nums, [])
        return res