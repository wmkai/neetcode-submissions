class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            leng = int(s[i:j])
            j += 1
            cur_s = s[j:j + leng]
            res.append(cur_s)
            i = j + leng
        return res

