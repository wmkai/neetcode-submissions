class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] <= nums[mid]: # 左边有序
                if nums[mid] == target:
                    return mid
                elif nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] == target:
                    return mid
                if nums[mid] < target <= nums[r]:
                    l = mid
                else:
                    r = mid - 1
        return -1