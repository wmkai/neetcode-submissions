class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in hashmap or hashmap[t[i]] == 0:
                return False
            else:
                hashmap[t[i]] -= 1
        for val in hashmap.values():
            if val != 0:
                return False
        return True
