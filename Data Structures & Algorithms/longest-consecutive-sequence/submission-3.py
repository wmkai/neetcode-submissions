class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 题意：找到最长连续子序列的长度（连续的意思是+1）
        # O(n)解法：先把数组里所有元素记录到hashmap中，然后遍历hashmap
        # 仅当这个数前面没有相邻元素时，计算以这个数为起点，最长的连续子序列长度
        hashmap = {}
        res = 0
        for i in range(len(nums)): # 先把数组里所有元素记录到hashmap中
            hashmap[nums[i]] = 1
        for num in hashmap.keys(): # 遍历hashmap
            if num - 1 not in hashmap: # 仅当这个数前面没有相邻元素时
                cur_len = 1
                while num + 1 in hashmap: # 以这个数为起点，最长的连续子序列长度
                    cur_len += 1
                    num += 1
                res = max(res, cur_len)
        # 仅当这个数前面没有相邻元素时才计算，前面有相邻元素就跳过。所以即使for里有个while，时间也是O(n)
        return res