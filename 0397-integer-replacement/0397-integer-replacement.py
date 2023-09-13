class Solution:
    def integerReplacement(self, n: int) -> int:
        dp = {}
        def helper(num):
            if num == 1:
                return 0
            if num in dp:
                return dp[num]
            if num % 2 == 0:
                dp[num] = 1 + helper(num // 2)
            else:
                dp[num] = 1 + min(helper(num + 1), helper(num - 1))
            return dp[num]
        return helper(n)