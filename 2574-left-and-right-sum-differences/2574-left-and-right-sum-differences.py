class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums)
        for i in range(n):
           
            s = abs(sum(nums[:i])-sum(nums[i+1:]))
            arr.append(s)
        return arr