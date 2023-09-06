class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = []
        r = len(matrix)
        c = len(matrix[0])
        for i in range(c):
            row = []
            for j in range(r):
                row.append(matrix[j][i])
            m.append(row)
        
        
        return m