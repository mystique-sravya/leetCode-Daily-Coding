class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 1
        h = x
        while(l <= h):
            m =l+ (h-l)//2
            if m*m == x:
                return m
            elif m*m > x:
                h = m - 1
            else:
                l = m+1
        return h
                