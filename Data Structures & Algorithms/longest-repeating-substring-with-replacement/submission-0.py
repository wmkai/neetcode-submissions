class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        window = {}
        max_freq = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in window:
                window[s[i]] = 1
            else:
                window[s[i]] += 1
            max_freq = max(max_freq, window[s[i]])
            while max_freq < i - j + 1 - k:
                window[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res
            
