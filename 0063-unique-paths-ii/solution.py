class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1]*n for _ in range(m)]
        def solver(i,j):
            if i==0 and j==0 and obstacleGrid[i][j]!=1:
                return 1
            if i==0 and j==0 and obstacleGrid[i][j]!=0:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
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
        return solver(m-1,n-1)
            
        