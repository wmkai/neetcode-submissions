class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 求排列，使用新的数组作为递归参数，比较方便
        res = []
        def dfs(cur_nums, ans): # 注意：不能用nums，不然会和外面的变量重名
            if len(ans) == len(nums): # 等价于if not cur_nums:
                res.append(ans)
            else:
                for i in range(len(cur_nums)):
                    # 和求组合不一样，这里新数组只要不包含当前元素就可以了
                    dfs(cur_nums[:i] + cur_nums[i+1:], ans + [cur_nums[i]])
                    # 注意：两个list拼接，相加就好；如果是list和单个元素拼接，需要把单个元素先用list包装起来
        dfs(nums, [])
        return res
        