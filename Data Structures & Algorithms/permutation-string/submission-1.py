class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 题意：在字符串s2中能否找到字符串s1的一种排列
        # 思路：滑动窗口模板题
        window, need = {}, {} # 窗口内元素 和 所需元素
        valid = 0 # window内有效字符的个数
        res = []
        for c in s1: # 所需元素
            if c not in need:
                need[c] = 0
            need[c] += 1

        j = 0 # 窗口左边界
        for i, c in enumerate(s2): # i模拟窗口右边界下标
            if c not in window:
                window[c] = 0
            window[c] += 1
            if c in need and window[c] <= need[c]: # 窗口内c元素比所需c元素少
                valid += 1 # 说明c是个有效元素
            # 窗口长度相等，就缩小，因此只有一次，不需要while，缩小前要判断是否满足条件
            if i - j + 1 == len(s1): # 注意：下标相减后要+1
                if valid == len(s1): # 有效字符个数和s1中一样
                    return True # 找到解
                d = s2[j] # 即将移除的元素
                window[d] -= 1
                if d in need and window[d] < need[d]: # d移出后窗口内d数量小于所需d数量
                    valid -= 1 # 说明d是个有效元素，所以有效元素-1
                j += 1 # 窗口缩小
        return False