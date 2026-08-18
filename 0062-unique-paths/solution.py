class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
         dp = [[-0] * n for _ in range(m)]
         dp[m-1][n-1]=1
         for i in range(n):
            dp[m-1][i]=1
         for j in range(m):
            dp[j][n-1]=1
         for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
         return dp[0][0]

'''
        dp = [[-1] * n for _ in range(m)]
        
        def solver(i, j):

            if i == m - 1 and j == n - 1:
        
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            right = 0
            down = 0

            if j + 1 < n:
                right = solver(i, j + 1)

            if i + 1 < m:
                down = solver(i + 1, j)

            dp[i][j] = right + down

            return dp[i][j]

        return solver(0, 0)'''
        