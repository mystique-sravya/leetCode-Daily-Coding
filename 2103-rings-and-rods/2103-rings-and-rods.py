class Solution:
    def countPoints(self, rings: str) -> int:
        c=0
        l=[""]*10
        for i in range(1,len(rings),+2):
            l[int(rings[i])]+=rings[i-1]
        for j in l:
            if 'R' in j and 'G' in j and 'B' in j:
                c+=1
        return c