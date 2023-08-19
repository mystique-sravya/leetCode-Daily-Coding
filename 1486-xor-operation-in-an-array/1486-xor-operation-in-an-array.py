class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
    
        for i in range(n):
            op = start+ 2*i
            res ^= op
        return res