class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        
        return [self.firstOcc(nums,target),self.lastOcc(nums,target)]
    
    def firstOcc(self, nums, target):
        ans = -1
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = (l+h)// 2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                h = mid-1
            else:
                ans = mid
                print(ans)
                h = mid-1
        return ans
    
    def lastOcc(self, nums, target):
        ans = -1
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = (l+h)// 2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                h = mid-1
            else:
                ans = mid
               
                l = mid+1
        return ans

                
                
                
                
            
            
        