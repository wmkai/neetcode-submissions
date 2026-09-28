class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        hashmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def dfs(idx, ans):
            if len(ans) == len(digits):
                res.append(ans)
                return
            print(hashmap[digits[idx]])
            for c in hashmap[digits[idx]]:
                dfs(idx + 1, ans + c)

        dfs(0, '')
        return res
