class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        window = {}
        j = 0
        for i in range(len(s)):
            if s[i] not in window:
                window[s[i]] = 1
            else:
                window[s[i]] += 1
            while (i - j + 1) - max(window.values()) > k:
                window[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res
            
