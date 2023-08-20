class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res = []
        
        for i in range(1, k+1):
            print(abs(i-k))
            if abs(i - k) not in res:
                res.append(i)
            print(res)
        if len(res) < n:
            for i in range(k+1, n+50):
                res.append(i)
            print(res)
        return sum(res[:n])