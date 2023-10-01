class Solution:
    def sortSentence(self, s: str) -> str:
        d=[]
        s=s.split()
        for x in s:
            d.append([x[:len(x)-1],int(x[len(x)-1])])
        #print(d)
        d=sorted(d,key=lambda x:x[1])
        #print(d)
        res=d[0][0]
        for i in range(1,len(d)):
            res+=" "+d[i][0]
        return res