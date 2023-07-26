class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            

            if target == nums[mid]:
                return True
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                    low = low + 1
                    high = high -1
                    continue
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False