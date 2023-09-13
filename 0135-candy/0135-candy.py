class Solution:
    def candy(self, r: List[int]) -> int:
        n = len(r)
        res = [1] * n
        for i in range(1, n):
            if r[i] > r[i - 1]:
                res[i] = res[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if r[i] > r[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)
        return sum(res)