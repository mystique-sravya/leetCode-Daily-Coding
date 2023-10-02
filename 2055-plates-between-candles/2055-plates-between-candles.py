class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle = []

        for i in range(len(s)):
            if s[i] == '|':
                candle.append(i)

        print(candle)

        def bs(idx):
            l, r = 0, len(candle)
            while l < r:
                m = l+(r-l)//2
                if candle[m]<idx:
                    l=m+1
                else:
                    r=m
            return l
        res = []
        for q in queries:
            left = bs(q[0])
            right = bs(q[1]+1)-1
            print(left, right)
            res.append(candle[right]-candle[left]-(right-left) if right>left else 0)
        return res