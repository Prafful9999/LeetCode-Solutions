class Solution:
    def beautySum(self, s: str) -> int:
        beauty=0
        for i in range(0,len(s)):
            freq=[0]*26
            for j in range(i,len(s)):
                ind=ord(s[j])-ord('a')
                freq[ind]+=1
                nonzero=[x for x in freq if x>0]
                if len(nonzero)>1:
                    beauty+=max(nonzero)-min(nonzero)
        return beauty

        