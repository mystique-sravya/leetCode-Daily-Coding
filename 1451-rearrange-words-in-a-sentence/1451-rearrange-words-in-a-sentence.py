class Solution:
    def arrangeWords(self, text: str) -> str:
        text=text.lower()
        s=text.split()
        s=sorted(s,key=lambda x : len(x))
        res=s[0][0].upper()
        res+=s[0][1:]
        for i in range(1,len(s)):
            res+=" "+s[i]
        return res