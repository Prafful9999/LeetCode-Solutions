class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[[-1]*n for _ in range(n)] for _ in range(m)]
        def solver(r,c1,c2):
            if c1<0 or c1>=n or c2<0 or c2>=n:
                return float('-inf')
            if dp[r][c1][c2]!=-1:
                return dp[r][c1][c2]
            if r==m-1:
                if c1==c2:
                    return grid[r][c1]
                else:
                    return grid[r][c1]+grid[r][c2]
            if c1==c2:
                curr=grid[r][c1]
            else:
                curr=grid[r][c1]+grid[r][c2]

            maxi=float('-inf')
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    maxi=max(maxi,solver(r+1,c1+i,c2+j))
            
            dp[r][c1][c2]=curr+maxi
            return dp[r][c1][c2]
            

            

        return solver(0,0,n-1)
