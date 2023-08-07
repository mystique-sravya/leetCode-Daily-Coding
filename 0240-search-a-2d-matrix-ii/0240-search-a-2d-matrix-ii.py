class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        k = target
        cr = 0
        cc = c-1
        while ( cr < r and cc >= 0):
            if matrix[cr][cc] == k:
                return True
            elif matrix[cr][cc] > k:
                cc -= 1
            else:
                cr += 1
        return False