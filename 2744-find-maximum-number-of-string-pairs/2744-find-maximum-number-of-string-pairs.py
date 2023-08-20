class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        d = {}
        c = 0
        for w in words:
            if w in d:
                c += 1
            else:
                d[w[::-1]] = w
                print(d)
        return c
        
        
        
        """
        strings = set()
        ans = 0
        for w in words:
            if w in strings:
                ans += 1
            else:
                strings.add(w[::-1])
                print(strings)
        return ans
        """