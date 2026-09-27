class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 本题的难点在于和39题的区别：
        # 1.39题一个元素可以多次选取，本题只能选取一次（可以通过把回溯函数的startindex由i改为i+1实现，树的下一层不选取访问过的节点）
        # 2.集合（数组candidates）有重复元素，而且结果中还不能有重复的组合。
        '''难点在于去重，“去重”在树形结构上是有两个维度的，一个维度是同一树枝上使用过，一个维度是同一树层上使用过。
        1.元素在同一个组合内是可以重复的，怎么重复都没事；
        2.但两个组合不能相同。
        所以我们要去重的是同一树层上的“使用过”，同一树枝上的都是一个组合里的元素，不用去重。
        用具体例子来说就是：
        1.可以选取[1,1,1,2]，但3个1都必须是candidates里的不同元素，树的每层可以看做是结果中的一个元素，因此同一树枝上是可以有相同元素的。
        2.同一树层上不能使用值相同元素的意思是，如果同一树层上使用了值一样的元素，比如：candidates中有两个1，就会分别使用这两个1作为结果中的第一个元素（而同一树枝上元素相同是分别用两个相同的元素作为结果的第一个和第二个元素，这样是可以的），这样就有可能得到重复解。
        '''
        # 对candidates排序后，我们碰到相同元素时candidates[i] == candidates[i-1]有两种情况
        # 1.同一树枝上 2.同一树层上
        # 我们可以使用一个used数组表示元素是否在自身所在树枝上被访问过，
        # 1.如果used[i-1]=1 and candidates[i] == candidates[i-1]，说明在树枝上被访问过，则可以再次访问
        # 2.如果used[i-1]=0 and candidates[i] == candidates[i-1]，说明在树干上被访问过，则不能再次访问
        # 具体思路参考https://programmercarl.com/0040.组合总和II.html#思路

        # 1. 使用新数组作为递归参数
        res = []
        candidates.sort()
        def dfs(nums, ans):
            if sum(ans) == target:
                res.append(ans)
            else:
                for i in range(len(nums)):
                    if sum(ans) + nums[i] > target: # 剪枝
                        break
                    if i > 0 and nums[i] == nums[i-1]: # 横向遍历要去重
                        continue
                    # 纵向递归一个元素只能取一次
                    dfs(nums[i+1:], ans + [nums[i]])
        dfs(candidates, [])
        return res

        # 2. 使用下标