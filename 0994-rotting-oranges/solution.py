class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        def bfs(r,c):
            nonlocal fresh
            if r<0 or r>rows-1 or c<0 or c>cols-1:
                return
            if grid[r][c] in [0,2]:
                return
            if grid[r][c]==1:
                grid[r][c]=2
                que.append((r,c))
                fresh-=1

        fresh=0
        rows=len(grid)
        cols=len(grid[0])
        que=deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    que.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        time=-1
        while len(que)!=0:
            size=len(que)
            print(len(que))
            for _ in range(size):
                r,c=que.popleft()
                bfs(r,c+1)
                bfs(r,c-1)
                bfs(r-1,c)
                bfs(r+1,c)  
            
            time+=1
            
        if fresh>0:
            return -1
        return time
                  
        