class Solution:
    def checkDivisibility(self, n: int) -> bool:
        N=n
        pro=1
        total=0
        while n>=1:
            digit=n%10
            total+=digit
            pro*=digit
            n=n//10
        ans=total+pro
        if N%ans!=0:
            return False
        else:
            return True


        