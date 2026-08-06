class Solution:
    def myAtoi(self, s: str) -> int:
        lst=[]
        i=0
        n=len(s)
        sign=1
        while i<n and s[i]==' ':
            i+=1
        if i<n and (s[i]=='-' or s[i]=='+'):
            if s[i]=='-':
                sign=-1
            i+=1
        while i<n and s[i].isdigit():
            lst.append(s[i])
            i+=1
        if not lst:
            return 0
        ans=sign*int(''.join(lst))
        int_min=-2**31
        int_max=2**31-1
        if ans<int_min:
            return int_min
        elif ans>int_max:
            return int_max
        else:
            return ans

            
        