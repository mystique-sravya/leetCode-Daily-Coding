class Solution:
    
    def calculatehr(self, piles, mid):
        th = 0
        n = len(piles)
        for i in range(n):
            th += ceil(piles[i]/mid)
        
        return th
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        hi = max(piles)
        ans =max(piles)
        while(l <= hi):
            m = (l+hi) // 2
            th = self.calculatehr(piles, m)
            if th <= h:
                ans =  m
                hi = m - 1
            else:
                l = m + 1
        return ans