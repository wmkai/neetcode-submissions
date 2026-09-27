class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # 用l和r记录左右括号的数量
        # 判断什么时候可以加入左、右括号
        # 1. 当左括号小于n，可加入左括号
        # 2. 当右括号小于左括号数量时，可以加入右括号
        def dfs(ans, l, r):
            nonlocal res
            if len(ans) == 2 * n:
                res.append(ans)
                return
            if l < n: # 注意：这里最容易出错，不是什么情况都可以加左括号
                dfs(ans + '(', l + 1, r)
            if r < l:
                dfs(ans + ')', l, r + 1)
            
        dfs('', 0, 0)
        return res
        