class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heap = []
        res = []
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        for (num, freq) in hashmap.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        for i in range(len(heap)):
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res