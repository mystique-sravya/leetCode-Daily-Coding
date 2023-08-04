class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        
        for i, v  in enumerate(nums):
            if v not in d:
                d[v] = i
            else:
                return True
        return False
    