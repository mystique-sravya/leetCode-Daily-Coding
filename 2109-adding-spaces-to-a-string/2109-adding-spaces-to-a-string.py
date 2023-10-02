class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = s 
        space_add=0 
        for i in spaces:
            j=i+space_add
            res = res[:j] + " " + res[j:] 
            space_add+=1
        return res