class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        N = len(deck)
        for x in range(2, N+1):
            if N % x == 0:
                if all(v % x == 0 for v in count.values()):
                    return True
        return False