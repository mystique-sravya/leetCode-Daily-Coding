class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in s:
            if i == "*":
                st.pop()
            else:
                st.append(i)
        w = ""
        if st == []:
            return ""
        else:
            while st != []:
                w += st.pop()
        return w[::-1]
            
            