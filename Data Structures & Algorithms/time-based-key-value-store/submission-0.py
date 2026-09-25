class TimeMap:

    def __init__(self):
        # key -> [(timestamp, value), ...]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 题目保证 set 的 timestamp 严格递增，
        # 所以可以直接 append，不需要额外排序
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # key 不存在
        if key not in self.store:
            return ''

        l, r = 0, len(self.store[key]) - 1

        # 二分查找：
        # 目标是找到 timestamp <= 查询时间 的最大 timestamp
        while l <= r:
            mid = l + (r - l) // 2
            mid_time = self.store[key][mid][0]

            # 正好找到目标时间，直接返回
            if mid_time == timestamp:
                return self.store[key][mid][1]

            # 当前时间太大，往左找
            elif mid_time > timestamp:
                r = mid - 1

            # 当前时间小于查询时间，
            # 说明它可能是答案，但继续往右找更大的合法 timestamp
            else:
                l = mid + 1

        # 循环结束后：
        # r 指向最后一个 timestamp <= 查询时间的位置
        # 如果 r < 0，说明查询时间比最早的 timestamp 还小
        if r < 0:
            return ''

        return self.store[key][r][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)