class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = 1
        for num in hashmap.keys():
            if num - 1 not in hashmap:
                cur = 1
                while num + 1 in hashmap:
                    cur += 1
                    num += 1
                res = max(res, cur)
        return res