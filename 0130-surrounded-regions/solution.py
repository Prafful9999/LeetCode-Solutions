class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        stack=[]
       

        
        def dfs(r,c):
            if r<0 or r>rows-1 or c<0 or c>cols-1:
                return 
            if board[r][c]=='X':
                return
            if board[r][c]=='#':
                return
            if board[r][c]=='O':
                board[r][c]='#'
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)

        for i in range(rows):
            if board[i][0]=='O':
               dfs(i,0)
            if board[i][cols-1]=='O':
                dfs(i,cols-1)
        for j in range(cols):
            if board[0][j]=='O':
                dfs(0,j)
            if board[rows-1][j]=='O':
                dfs(rows-1,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'
        
            


        