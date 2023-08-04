
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        i = len(s)
        while(i >= 0):
            s.append(s.pop(i-1))
            i -= 1