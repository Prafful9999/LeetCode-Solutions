class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        from collections import Counter
        htable2=Counter(t)
        need=len(htable2)
        have=0
        l=0
        htable1={}
        count=float('inf')
        res=[0]*2
        n=len(s)
        for r in range(n):
            htable1[s[r]]=htable1.get(s[r],0)+1
            if s[r] in htable2:
                if htable2[s[r]]==htable1[s[r]]:
                  have+=1
            while have==need:
                if r-l+1<count:
                    count=r-l+1
                    res=[l,r]
                htable1[s[l]]-=1
                if s[l] in htable2 and htable1[s[l]]<htable2[s[l]]:
                    have-=1
                l+=1
        if count!=float('inf'):
            return s[res[0]:res[1]+1]
        else:
            return ""
                    

        
        