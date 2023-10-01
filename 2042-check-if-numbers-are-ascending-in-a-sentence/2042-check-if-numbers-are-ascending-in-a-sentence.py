class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=[]
        s=s.split()
        for i in s:
            if i.isdigit():
                l.append(int(i))
        #print(l)
        for i in range(1,len(l)):
            if l[i-1]>=l[i]:
                return False
        return True