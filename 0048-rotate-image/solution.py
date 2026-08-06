class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r=len(matrix)
        for i in range(r-1):
            for j in range(r):
                if j>i:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(r):
            matrix[i].reverse()