class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
            row=len(matrix)
            column=len(matrix[0])
            rtrack=[]
            ctrack=[]
            for i in range(row):
                rtrack.append(0)
            for j in range(column):
                ctrack.append(0)
            for i in range(0,row):
                for j in range(0,column):
                    if matrix[i][j]==0:
                        rtrack[i]=-1
                        ctrack[j]=-1
            for i in range(0,row):
                for j in range(0,column):
                    if rtrack[i]==-1 or ctrack[j]==-1:
                        matrix[i][j]=0
                        

        