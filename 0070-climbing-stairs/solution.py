class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]
        '''
        def solver(ind):
            if ind==0 or ind==1:
                return 1
            if dp[ind]!=-1:
                return dp[ind]
            dp[ind]=solver(ind-1)+solver(ind-2)
            return dp[ind]
            
        return solver(n)'''