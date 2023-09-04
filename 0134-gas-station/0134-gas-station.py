class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        p = 0
        t = 0
        r = 0
        s = 0
        for i in range(len(gas)):
            p = p+ gas[i] - cost[i]
            t = t + gas[i]
            r = cost[i]
            if ( t-r < 0):
                t = 0
                s = i + 1
            else:
                t = t-r
        return s if p >= 0 else -1