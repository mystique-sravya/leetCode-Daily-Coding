class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        #brute:
        
        c = 0
        for word in words:
            b = 1
            for x in word:
                if x not in allowed:
                    b = 0
                    break
                else:
                    b = 1
                
                        
            if b == 1:
                c += 1
        return c
                
                
            