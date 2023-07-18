class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = set(nums)
        s = []
        for i in range(1,len(nums)+1):
            if i in l:
                continue
            s.append(i)
        return s