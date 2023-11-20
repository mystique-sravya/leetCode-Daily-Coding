class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time=[]
        time.append(0)
        for i in range(len(travel)):
                time.append(time[-1]+travel[i])
        res=0
        for type in ["P","G","M"]:
            cnt=0
            idx=0
            for i in range(len(garbage)):
                if type in garbage[i]:
                    # update index and count
                    idx=i
                    cnt+=garbage[i].count(type)
            res+=cnt+time[idx]
        return res