class Solution:
    def maxPower(self, s: str) -> int:
        mx = 1  
        curr = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                mx = max(mx, curr)
                curr = 1 

        return max(mx, curr)