class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)
        print(s)
    
        return s.count("1")
        