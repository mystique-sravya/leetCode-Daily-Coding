class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(n):
            s = n-i
            e = i + 1
            t = s * e
            o = (t+1)//2
            res = res + o * arr[i]
        return res
            
            
        