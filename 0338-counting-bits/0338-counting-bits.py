class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]
        for i in range(1,n+1):
            b = bin(i)[2:]
            arr.append(b.count("1"))
        return arr