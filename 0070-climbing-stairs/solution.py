class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def solver(ind):
            if ind==0 or ind==1:
                return 1
            if dp[ind]!=-1:
                return dp[ind]
            dp[ind]=solver(ind-1)+solver(ind-2)
            return dp[ind]
            
        return solver(n)