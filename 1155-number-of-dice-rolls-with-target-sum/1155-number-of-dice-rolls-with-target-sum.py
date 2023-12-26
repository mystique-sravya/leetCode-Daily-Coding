class Solution:
    mod = 1000000007

    def numRollsToTarget(self, n, k, target):
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        return self.helper(n, k, target, dp)

    def helper(self, n, k, target, dp):
        if n == 0 and target == 0:
            return 1
        if n == 0 or target <= 0:
            return 0
        if dp[n][target] != -1:
            return dp[n][target] % self.mod
        dp[n][target] = 0

        for i in range(1, k + 1):
            dp[n][target] = (dp[n][target] + self.helper(n - 1, k, target - i, dp)) % self.mod

        return dp[n][target]        