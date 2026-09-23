class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 题意：给一个字符串s，一个字符串t，返回s中涵盖t所有字符的最小子串
        # 思路：滑动窗口，分别用两个hashmap记录 所需字符数量 和 窗口内字符数量。当window中和need中匹配上一个字符时，匹配数valid +1。
        need, window = {}, {}
        valid = 0 # 记录need和window匹配上了几个不同的字符
        res, min_len = '', float('inf')
        
        for c in t: # 记录t中所有字符出现次数
            if c not in need:
                need[c] = 0
            need[c] += 1

        j = 0 # 模拟窗口左指针
        for i in range(len(s)): # 模拟窗口右指针
            c = s[i] # c 是将移入窗口的字符
            if c not in window:
                window[c] = 0
            window[c] += 1

            if c in need and window[c] <= need[c]: # c放入窗口后，c是否够了
                valid += 1 # 当window和need中，匹配上时，valid+1

            while valid == len(t): # 都匹配上时，说明可以缩小左窗口
                if i - j + 1 < min_len: # 判断当前符合条件的字符串是否满足最小长度
                    min_len = i - j + 1 # 更新最小长度
                    res = s[j: i+1] # 记录答案
                d = s[j] # 先记录要被踢出的左窗口元素
                window[d] -= 1 # 先移除再判断，或者先判断再移除都可以，区别就是≤和<
                if d in need and window[d] < need[d]: # 这里是判断把d移除窗口前，如果当前窗口内d的数量和需要的d的数量相等，那么l右移后肯定就不相等了
                    valid -= 1 # 匹配数-1
                j += 1 # j右移
        return res # 如果没找到，就直接返回空字符串''