class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort(mat, r, c, i , j):
            m = i
            n = j
            l= []
            while(m < r and n < c):
                l.append(mat[m][n])
                m = m + 1
                n = n +1
            l.sort()
            m = i
            n = j
            idx = 0
            while(m < r and n < c):
                mat[m][n] = l[idx]
                idx += 1
                m += 1
                n +=1 
               
        r = len(mat)
        c = len(mat[0])
        for i in range(c):
            sort(mat,r,c,0,i)
        for i in range(1,r):
            sort(mat,r,c,i, 0)
        return mat