class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        c = 1 
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                c += 1
            else:
                res+= c * (c + 1) // 2
                res= res% MOD
                c = 1
        res+= c * (c + 1) // 2
        res= res% MOD
        
        return res