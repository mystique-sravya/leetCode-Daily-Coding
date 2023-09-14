class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count1=Counter(s)
        res=0
        check=True
        while(check):
            for ch in target:
                if(count1[ch]>0):
                    count1[ch]-=1
                elif(count1[ch]==0):
                    check=False
                    break
            if(check):      
                res+=1
        return res