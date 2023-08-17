class Solution:
    def repeatedCharacter(self, s: str) -> str:
        se = set()
        for i in s:
            if i in se:
                return i
            else:
                se.add(i)