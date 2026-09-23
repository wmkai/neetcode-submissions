class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        need = {}
        valid = 0
        res = ''
        min_len = float('inf')
        j = 0
        for i in range(len(t)):
            if t[i] not in need:
                need[t[i]] = 0
            need[t[i]] += 1
        for i in range(len(s)):
            if s[i] not in window:
                window[s[i]] = 0
            window[s[i]] += 1
            if s[i] in need and window[s[i]] <= need[s[i]]:
                valid += 1
            while valid == len(t):
                if i - j + 1 < min_len:
                    min_len = i - j + 1
                    res = s[j:i+1]
                d = s[j]
                if d in need and window[d] <= need[d]:
                    valid -= 1
                window[d] -= 1
                j += 1
        return res