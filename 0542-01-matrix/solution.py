class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        rows=len(mat)
        cols=len(mat[0])
        que=deque([])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    que.append((i,j))
                elif mat[i][j]==1:
                    mat[i][j] = -1
        while que:
            r,c=que.popleft()
            if r - 1 >= 0 and mat[r - 1][c] == -1:
                mat[r - 1][c] = mat[r][c] + 1
                que.append((r - 1, c))

            if r + 1 < rows and mat[r + 1][c] == -1:
                mat[r + 1][c] = mat[r][c] + 1
                que.append((r + 1, c))

            if c - 1 >= 0 and mat[r][c - 1] == -1:
                mat[r][c - 1] = mat[r][c] + 1
                que.append((r, c - 1))

            if c + 1 < cols and mat[r][c + 1] == -1:
                mat[r][c + 1] = mat[r][c] + 1
                que.append((r, c + 1))
        return mat
           




            