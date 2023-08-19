class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        i = n - 1
        j = 0
        while(s[i] == " "):
            i -= 1
        while( i >= 0 and s[i] != " "):
            j += 1
            i -= 1
        return j