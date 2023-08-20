class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        row1= s[0]
        col1 = int(s[1])
        row2 = s[3]
        col2 = int(s[4])
        l = []
           
        for j in range(ord(row1),ord(row2)+1):
            for i in range(col1,col2+1):
                rc = chr(j)+str(i)
                l.append(rc)
        
        return l