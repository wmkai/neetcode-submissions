class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        res = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in window:
                window[s[i]] = 1
            else:
                window[s[i]] += 1
            while window[s[i]] > 1:
                window[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res
                
