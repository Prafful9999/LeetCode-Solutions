class Solution:
    def findRotation(self, mat, target):
        
        def rotate(matrix):
            n = len(matrix)
            
            # 👉 Transpose
            for row in range(n):
                for col in range(row + 1, n):
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            
            # 👉 Reverse each row
            for row in matrix:
                row.reverse()
            
            return matrix
        
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)   # in-place change
        
        return False