class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        max_num = float(-inf)
        for n in nums:
            max_num =max(max_num,n)
        
        n = len(nums)
        res = [-1]*n
        temp = nums*2
        for  i in range(n):
            if nums[i] == max_num:
                continue
            for j in range(i+1, n*2):
                if temp[j] > nums[i]:
                    res[i] = temp[j]
                    break
        return res