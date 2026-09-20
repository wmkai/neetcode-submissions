class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in hashmap:
                hashmap[ss] = [s]
            else:
                hashmap[ss].append(s)
        for val in hashmap.values():
            res.append(val)
        return res
        