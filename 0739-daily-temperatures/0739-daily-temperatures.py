class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        arr = [0]*len(T)
        s = deque()
        for curr in range(len(T)-1,-1,-1):
            while s and T[s[-1]] <= T[curr]:
                s.pop()
            arr[curr] = s[-1]-curr if s else 0
            s.append(curr)
        return arr 
    