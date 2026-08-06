class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        
        if n < 0:
            x = 1 / x
            n = -n
        
        def solve(a):
            if a == 1:
                return x
            
            ans = solve(a // 2)
            
            if a % 2 == 0:
                return ans * ans
            else:
                return x * ans * ans
        
        return solve(n)
