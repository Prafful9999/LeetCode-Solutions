class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        prev=[0]*n
        for i in range(m):
            curr=[0]*n
            for j in range(n):
                if i==0 and j==0:
                    curr[0]=grid[0][0]
                    continue
                up=float('inf')
                left=float('inf')
                if i-1>=0:
                    up=prev[j]
                if j-1>=0:
                    left=curr[j-1]
                curr[j]=grid[i][j]+min(up,left)
            prev=curr.copy()
        return prev[-1]
        
        '''

        dp=[[-1]*n for _ in range(m)] 
        dp[0][0]=grid[0][0]
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j==0:
                    continue
                up=float('inf')
                left=float('inf')
                if i-1>=0:
                    up=dp[i-1][j]
                if j-1>=0:
                    left=dp[i][j-1] 
                dp[i][j]=grid[i][j]+min(up,left)
        return dp[m-1][n-1]

        
        dp=[[-1]*n for _ in range(m)]
        def solver(i,j):
            if i==0 and j==0:
                return grid[i][j] 
            if dp[i][j]!=-1:
                return dp[i][j]
            up=float('inf')
            left=float('inf')
            if i-1>=0:
                up=solver(i-1,j)
            if j-1>=0:
                left=solver(i,j-1)
            dp[i][j]=grid[i][j]+min(up,left)
            return dp[i][j]
        return solver(m-1,n-1)'''
