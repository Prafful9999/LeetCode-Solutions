class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        else:
            if n==1:
                return x
            if n==-1:
                return 1/x
            if n%2==0:
                x= self.myPow(x,n//2)
                return x*x
            else:
                if n>0:
                    ans=self.myPow(x,(n-1)//2)
                    return x*ans*ans
                else:
                    ans=self.myPow(x,(n+1)//2)
                    return (1/x)*ans*ans
        