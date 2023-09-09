class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n  = len(heights)
        res = [0] * n
        s = []
        for i in range(n-1,-1,-1):
            height = heights[i]
            v = 0
            while s and height > s[-1]:
                v += 1
                s.pop()
            if s:
                v += 1
            res[i] = v
            s.append(height)
        return res