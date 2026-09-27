class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def dfs(cur_s, ans):
            if not cur_s:
                res.append(ans)
            for i in range(len(cur_s)):
                if is_palindrome(cur_s[:i+1]):
                    dfs(cur_s[i+1:], ans + [cur_s[:i+1]])
        
        dfs(s, [])
        return res
