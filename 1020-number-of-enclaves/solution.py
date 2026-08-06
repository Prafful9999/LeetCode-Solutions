class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        stack=[]
        for i in range(rows):
            if grid[i][0]==1:
                stack.append((i,0))
            if grid[i][cols-1]==1:
                stack.append((i,cols-1))
        for j in range(cols):
            if grid[0][j]==1:
                stack.append((0,j))
            if grid[rows-1][j]==1:
                stack.append((rows-1,j))
        
        def mark(r,c):
            if r<0 or r>rows-1 or c<0 or c>cols-1:
                return
            if grid[r][c] in [0,-1]:
                return
            grid[r][c]=-1
            mark(r,c-1)
            mark(r,c+1)
            mark(r-1,c)
            mark(r+1,c)
            
        while stack:
            r,c=stack.pop()
            mark(r,c)
        

        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    count+=1
        return count
        