class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dp = [-1]*len(s)
        for i in range(1,len(s)):
            res = s[:i].find(s[i])
            if res == -1: 
                dp[i] = dp[i-1]
                continue
            dp[i] = max(dp[i-1],i-res-1)
        return dp[-1]