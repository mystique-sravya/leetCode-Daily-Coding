class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        l = len(n)
        s = 0
        for i in range(l):
            if  i % 2 == 0 :
                s += int(n[i])
            else:
                s -= int(n[i])
        return s
                
                