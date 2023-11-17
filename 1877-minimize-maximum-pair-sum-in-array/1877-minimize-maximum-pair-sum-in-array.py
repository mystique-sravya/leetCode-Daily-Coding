class Solution:
    def minPairSum(self, A: List[int]) -> int:
        return max(a + b for a, b in zip(sorted(A), sorted(A)[::-1]))
