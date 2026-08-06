class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_max=2**31
        int_min=-2**31
        sign=1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            sign=-1
        n=abs(dividend)
        x=abs(divisor)
        ans=0
        while n>=x:
            count=0
            while n>=x<<(count+1):
                count+=1
            ans+=1<<count
            n=n-(x<<count)
        if ans>=int_max and sign==1:
            return sign*(int_max-1)
        elif ans>=int_max and sign==-1:
            return sign*int_max
        else:
            return sign*ans        



        