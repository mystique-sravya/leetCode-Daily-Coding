class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        j = 0
        while j < len(s):
            
            if j + k <= len(s):
                res += s[j:j + k][::-1]
            else:
                res += s[j:][::-1]
            j += k

            
            if j < len(s):
                res += s[j:j + k]
            j += k

        return res