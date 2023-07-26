class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        l = []
        c = ""
        
        for i in nums:
            c += str(i)
            if int(c,2) % 5 == 0:
                l.append(True)
            else:
                l.append(False)
        return l
        