class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [[-1] * n for _ in range(n)]

        # First row
        for j in range(n):
            dp[0][j] = matrix[0][j]

        # Remaining rows
        for i in range(1, n):
            for j in range(n):

                up = dp[i-1][j]

                up_left = float('inf')
                up_right = float('inf')

                if j-1 >= 0:
                    up_left = dp[i-1][j-1]

                if j+1 < n:
                    up_right = dp[i-1][j+1]

                dp[i][j] = matrix[i][j] + min(up, up_left, up_right)

        return min(dp[n-1])
            
'''
        def dp(r,c):
            if r==0:
                return matrix[r][c]
            up=float('inf')
            up_left=float('inf')
            up_right=float('inf')
            if dp[r][c]!=-1:
                return dp[r][c]
            up=dp(r-1,c)
            if c-1>=0:
                up_left=dp(r-1,c-1)
            if c+1<n:
                up_right=dp(r-1,c+1)
            dp[r][c]=matrix[r][c]+min(up,up_left,up_right)
            return dp[r][c]
        ans=float('inf')
        for i in range(n):
            ans=min(ans,dp(n-1,i))
        return ans
'''
        