class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        avg = []
        for i in range(n//2):
            avg.append((nums[0] + nums[-1])/2)
            nums.pop(0)
            nums.pop(-1)
            
        return len(set(avg))
            