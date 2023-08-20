class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = nums.count(i)
        
        l =[]
        for k,v in d.items():
            if v == 1:
                l.append(k)
        return l