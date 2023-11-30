class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        vals = [(1 << b + 1) - 1 for b in range(30, -1, -1) if (1 << b) & n]
        return sum(sb * (-1 if i % 2 else 1) for i, sb in enumerate(vals))