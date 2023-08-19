class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        res = start ^ goal
        c = 0
        while res:
            res &= res  - 1
            c += 1
        return c
        """
        return (start ^ goal).bit_count()
            