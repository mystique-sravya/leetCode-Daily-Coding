class Solution:
    def balancedStringSplit(self, S: str) -> int:
        m = c = 0
        for s in S:
            if s == 'L': c += 1
            if s == 'R': c -= 1
            if c == 0: m += 1
        return m


        """
        m, c, D = 0, 0, {'L':1, 'R':-1}
        for s in S: c, m = c + D[s], m + (c == 0)
        return m
        """