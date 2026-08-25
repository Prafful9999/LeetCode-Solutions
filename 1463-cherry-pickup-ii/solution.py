class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        prev=[[-1]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    prev[i][j]=grid[m-1][i]
                else:
                    prev[i][j]=grid[m-1][i]+grid[m-1][j]
        for i in range(m-2,-1,-1):
            curr=[[-1]*n for _ in range(n)]
            for j in range(n):
                for k in range(n):
                    if j==k:
                        curr_ele=grid[i][j]
                    else:
                        curr_ele=grid[i][j]+grid[i][k]
                    maxi=float('-inf')
                    for a in [-1,0,1]:
                        for b in [-1,0,1]:
                            new_j=j+a
                            new_k=k+b
                            if new_j<0 or new_j>=n or new_k<0 or new_k>=n:
                                continue
                            maxi=max(maxi,prev[new_j][new_k])
                    curr[j][k]=curr_ele+maxi
            prev=curr
        return prev[0][n-1]
        

    '''
        for i in range(n):
            for j in range(n):
                if i==j:
                    dp[m-1][i][j]=grid[m-1][i]
                else:
                    dp[m-1][i][j]=grid[m-1][i]+grid[m-1][j]
        for i in range(m-2,-1,-1):
            for j in range(n):
                for k in range(n):
                    if j==k:
                        curr=grid[i][j]
                    else:
                        curr=grid[i][j]+grid[i][k]
                    maxi=float('-inf')
                    for a in [-1,0,1]:
                        for b in [-1,0,1]:
                            new_j=j+a
                            new_k=k+b
                            if new_j<0 or new_j>=n or new_k<0 or new_k>=n:
                                continue
                            maxi=max(maxi,dp[i+1][j+a][k+b])
                    dp[i][j][k]=curr+maxi
        return dp[0][0][n-1]
                    


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
        '''
