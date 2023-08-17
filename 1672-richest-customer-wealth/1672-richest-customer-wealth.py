class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        maxw = 0
        for i in range(n):
            sm = sum(accounts[i])
            maxw = max(maxw,sm)
        return maxw
                