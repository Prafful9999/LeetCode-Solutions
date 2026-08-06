class Solution:
    def beautySum(self, s: str) -> int:
        lst=[]
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                lst.append(s[i:j+1])
        def beauty(string1):
            htable={}
            for i in string1:
                if i not in htable:
                    htable[i]=1
                else:
                    htable[i]+=1
            l=htable.values()
            return max(l)-min(l)
        ans=0
        for i in lst:
            val=beauty(i)
            if val>=0:
                ans+=val
        return ans

                
        