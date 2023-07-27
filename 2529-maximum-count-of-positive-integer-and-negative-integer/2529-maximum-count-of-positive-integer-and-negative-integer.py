class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)
        
        l = 0
        h = len(nums) - 1
        nc = 0
        pc = 0
        while(l <= h):
            m = (l+h) //2
            if nums[m] < 0:
                nc = m +1
                l = m + 1
            else:
                h = m- 1
        
        l = 0
        h = len(nums) - 1
        while(l <= h):
            m = (l+h)//2
            if nums[m] > 0:
                pc = len(nums)- m
                h = m - 1
            else:
                l = m + 1
        
        return max(pc, nc)
        
       