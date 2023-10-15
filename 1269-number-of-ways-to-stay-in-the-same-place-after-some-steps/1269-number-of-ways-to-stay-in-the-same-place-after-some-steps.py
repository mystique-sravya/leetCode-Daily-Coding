class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps + 1)
        prev = [1] + [0] * (arrLen - 1)
        cur = [0] * arrLen
        for i in range(1, steps + 1):     
            for j in range(arrLen):
                cur[j] = 0
                cur[j] += prev[j]
                if j > 0:
                    cur[j] += prev[j - 1]
                if j < arrLen - 1:
                    cur[j] += prev[j + 1]
            prev, cur = cur, prev
        return prev[0] % (10 ** 9 + 7)