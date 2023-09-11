class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for i in s:
            if st and i == st[-1]:
                st.pop()
            else:
                st.append(i)
        w = ''
        if st == []:
            return ""
        else:
            while st:
                w += st.pop()
        return w[::-1]