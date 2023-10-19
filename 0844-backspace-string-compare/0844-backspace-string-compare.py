class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for i in s:
            if i != '#':
                s1.append(i)
            else:
                if s1 == []:
                    continue
                s1.pop()
        for i in t:
            if i != '#':
                s2.append(i)
            else:
                if s2 == []:
                    continue
                s2.pop()
        return s1 == s2