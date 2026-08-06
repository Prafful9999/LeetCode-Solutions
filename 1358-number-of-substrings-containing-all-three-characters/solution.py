class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        ans=0
        htable={'a':0,'b':0,'c':0}
        n=len(s)
        for r in range(n):
            htable[s[r]]+=1   
            while htable['a']>=1 and htable['b']>=1 and htable['c']>=1:
                ans+=n-r
                htable[s[l]]-=1
                l+=1
                
        return ans


        