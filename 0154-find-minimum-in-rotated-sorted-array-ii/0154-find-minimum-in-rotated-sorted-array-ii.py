class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high = 0,len(nums)-1
        while low < high:
            mid = low + int((high-low)/2)
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else: 
                high = high - 1
        return nums[low]