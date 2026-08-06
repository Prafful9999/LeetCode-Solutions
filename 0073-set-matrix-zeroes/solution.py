class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
    
        row_marker = [0]*rows
        col_marker = [0]*cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    row_marker[r] = -1
                    col_marker[c] = -1

        print(row_marker, col_marker)
                    

        for r in range(rows):
            for c in range(cols):
                if row_marker[r] == -1 or col_marker[c] == -1:
                    matrix[r][c]=0
        print(matrix)

        return matrix

        # for r in range(0, rows):
        #     for c in range(0, cols):
        #         if row_marker[r] == -1 or col_marker[c] ==-1:
        #             matrix[r][c] = 0






    #optimal
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     rows = len(matrix)
    #     cols = len(matrix[0])
    #     row_track = [0]*rows
    #     col_track = [0]*cols
    #     print(row_track, col_track)

    #     for r in range(0, rows):
    #         for c in range(0, cols):
    #             if matrix[r][c] == 0:
    #                 row_track[r] = -1
    #                 col_track[c] = -1

    #     print(row_track, col_track)


    #     for r in range(0, rows):
    #         for c in range(0, cols):
    #             if row_track[r] == -1 or col_track[c] ==-1:
    #                 matrix[r][c] = 0

    #     return matrix


















    # def markinf(self, mat, r, c):
    #     rows = len(mat)
    #     cols = len(mat[0])

    #     for rw in range(0, rows):
    #         if mat[rw][c] != 0:
    #             mat[rw][c] = float('inf')

    #     for cl in range(0, cols):
    #         if mat[r][cl]!=0:
    #             mat[r][cl] = float('inf')
        
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     rows = len(matrix)
    #     cols = len(matrix[0])

    #     for r in range(0, rows):
    #         for c in range(0, cols):
    #             if matrix[r][c]==0:
    #                 self.markinf(matrix, r, c)

    #     print(matrix)

    #     for r in range(0, rows):
    #         for c in range(0, cols):
    #             if matrix[r][c]==float('inf'):
    #                 matrix[r][c] = 0



    







































    #optimal
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     rows = len(matrix)
    #     cols = len(matrix[0])
    #     row_track = [0]*rows
    #     col_track = [0]*cols
    #     print(row_track, col_track)

    #     for r in range(0, rows):
    #         for c in range(0, cols):
    #             if matrix[r][c] == 0:
    #                 row_track[r] = -1
    #                 col_track[c] = -1

    #     print(row_track, col_track)


    #     for r in range(0, rows):
    #         for c in range(0, cols):
    #             if row_track[r] == -1 or col_track[c] ==-1:
    #                 matrix[r][c] = 0

    #     return matrix


        
                    







    #Brute
    # def convzero(self, matrix, r, c):
    #         print(r,c)
    #         rows = len(matrix)
    #         cols = len(matrix[0])

    #         for c1 in range(0, cols):
    #             if matrix[r][c1] != 0:
    #                 matrix[r][c1] = float('-inf')

    #         for r1 in range(0, rows):
    #             if matrix[r1][c] != 0:
    #                 matrix[r1][c] = float('-inf')


    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     # print(matrix) 
    #     rows = len(matrix)
    #     cols = len(matrix[0])
    #     for r in range(0, rows):
    #         for c in range(0, cols):
    #             if matrix[r][c] ==0 :
    #                 self.convzero(matrix, r, c)

    #     print(matrix)


    #     for r in range(0, rows):
    #         for c in range(0, cols):
    #             if matrix[r][c] == float('-inf') :
    #                 matrix[r][c] = 0

    #     return matrix




        