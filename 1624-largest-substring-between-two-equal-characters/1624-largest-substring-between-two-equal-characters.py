class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d=Counter(s)
        res=[]
        c=0
        for i in d.keys():
            if d[i]>=2:
                c+=1
                res.append(i)
        ans=[]
        if c==0:return -1
        for i in res:
            x=s.find(i)
            y=s.rfind(i)
            if x!=-1 and y!=-1:
                ans.append( y-x-1)
        return max(ans)
