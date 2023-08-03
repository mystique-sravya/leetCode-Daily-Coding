class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = nums.count(i)
            
        for k,v in d.items():
            if v > len(nums)//2:
                return k
            
                
        