class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue
                if i==0 and j==0:
                    continue
                up=0
                left=0
                if i-1>=0:
                    up=dp[i-1][j]
                if j-1>=0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
        return dp[-1][-1]
        '''
        dp=[[-1]*n for _ in range(m)]
        def solver(i,j):
             if obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
           
            if dp[i][j]!=-1:
                return dp[i][j]
            up=0
            left=0
            if i-1>=0:
                up=solver(i-1,j)
            if j-1>=0:
                left=solver(i,j-1)
            dp[i][j]=up+left
            return dp[i][j]
        return solver(m-1,n-1)'''
            
        