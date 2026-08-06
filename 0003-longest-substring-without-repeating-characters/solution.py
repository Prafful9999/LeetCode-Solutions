class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        mydict={}
        ans=0
        while r<len(s):
            if s[r] in mydict:
                l=max(l,mydict[s[r]]+1)
                
            mydict[s[r]]=r
            ans=max(ans,r-l+1)
            r+=1
            
        return ans
        