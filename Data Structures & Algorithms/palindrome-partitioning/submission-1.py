class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 因为s的长度最大只有16，所以用回溯法暴力搜索
        res = []
        def is_palindrome(s): # 判断s是否是回文串
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(string, ans):
            if not string: # 若字符串用完了，说明之前的子串都是回文串，找到一种分割结果
                res.append(ans)
            for i in range(len(string)): # i为当前字符串结束下标
                if is_palindrome(string[:i+1]): # 若string[:i+1]是回文
                    # 把string[:i+1]加入结果，并对剩下字符串string[i+1:]进行递归
                    dfs(string[i+1:], ans + [string[:i+1]])
        dfs(s, [])
        return res        