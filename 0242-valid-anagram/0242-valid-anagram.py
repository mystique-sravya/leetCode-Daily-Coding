class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        for i in s:
            if i not in d1:
                d1[i] = s.count(i)
        
        d2 = {}
        for i in t:
            if i not in d2:
                d2[i] = t.count(i)
        
        return d1 == d2
        