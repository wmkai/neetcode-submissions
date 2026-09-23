class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        need = {}
        valid = 0
        j = 0
        for i in range(len(s1)):
            if s1[i] not in need:
                need[s1[i]] = 1
            else:
                need[s1[i]] += 1
        for i in range(len(s2)):
            if s2[i] not in window:
                window[s2[i]] = 1
            else:
                window[s2[i]] += 1
            if s2[i] in need and window[s2[i]] <= need[s2[i]]:
                valid += 1
            if i - j + 1 > len(s1):
                if s2[j] in need and window[s2[j]] <= need[s2[j]]:
                    valid -= 1
                window[s2[j]] -= 1
                j += 1
            if valid == len(s1):
                return True
        return False
        