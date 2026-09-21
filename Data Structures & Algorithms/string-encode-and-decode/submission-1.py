class Solution:
    # 题意：把一组字符串编码成一个字符串，再能无歧义地还原回来。
    # 最稳的做法是给每个字符串加上「长度前缀」：
    # ["lint", "code", "love", "you"]
    # 编码成：4#lint4#code4#love3#you
    # 这样即使原字符串里面自己包含 # , 空格，都不怕，因为 decode 时我们不是靠分隔符切字符串，而是靠长度读取。
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # 在一个字符串里找字符串，一般都是用嵌套while循环
        while i < len(s):
            j = i
            # 找到 #
            while s[j] != '#':
                j += 1
            # i 到 j-1 是字符串长度
            leng = int(s[i:j])
            # 真正字符串从 j + 1 开始
            j += 1
            cur_s = s[j:j + leng]
            res.append(cur_s)
            i = j + leng
        return res

