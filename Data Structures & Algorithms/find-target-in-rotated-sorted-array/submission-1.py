class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """总体思路：一共有几种情况：
        1. 中间元素=target，返回下标（以下两种情况，都是中间元素!=target，这时候要把中间元素和左端点元素对比，确定哪边才是有序区间）
        2. 中间元素>左端点元素，说明左半边[l,mid]有序
            2.1. 左端点元素<=target<中间元素，说明target在左半边有序区间里，r=mid-1
            2.2. 否则，target在右半边无序区间，l=mid+1
        3. 中间元素<左端点元素，说明右半边[mid,r]有序
            3.1. 中间元素<target<=右端点元素，说明target在右半边有序区间里，l=mid+1
            3.3. 否则，target在左边板无序区间，r=mid-1
        """
        # 知道思路后，要处理好边界，使用while l<=r
        # 使用闭区间，因此更新l和r时，要l=mid+1，r=mid-1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= nums[l]: # mid元素属于左半边有序子数组
            # 注意：这个等号不能去掉（这是最容易错的地方）
            # 由于//是下取整，因此数组长度为偶数时，mid = (l + r) // 2是在左半边的。
            # 举例：当有2个元素[3,1]，mid是第0位，属于左边。此时l=mid=0
            # 左边虽然只有1个元素，但也是有序的。
            # 如果把if判断中等号去掉，nums[0] > nums[0]导致不满足左半边有序的条件，显然是不对的
                if nums[mid] == target: # 在中间
                    return mid
                elif nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # mid元素属于右半边有序子数组
                if nums[mid] == target: # 在中间
                    return mid
                elif nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1 # 找不到，要返回-1