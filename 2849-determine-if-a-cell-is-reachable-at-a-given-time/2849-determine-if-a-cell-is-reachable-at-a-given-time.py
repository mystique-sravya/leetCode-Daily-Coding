class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x = abs(fx - sx)
        y = abs(fy - sy)
        maxxy= max(x, y)

        if maxxy > t or (maxxy == 0 and (0 < t < 2)):
            return False
        else:
            return True