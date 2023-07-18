class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0
        n = len(timeSeries)
        if n == 0:
            return 0
        total = 0
        for i in range(n-1):
            total += min(timeSeries[i+1] - timeSeries[i], duration)
        return total + duration