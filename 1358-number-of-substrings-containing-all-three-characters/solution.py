class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        ans=0
        arr=[0]*3
        n=len(s)
        for r in range(n):
            arr[ord(s[r])-ord('a')]+=1
            while arr[0]>0 and arr[1]>0 and arr[2]>0:
                ans+=n-r
                arr[ord(s[l])-ord('a')]-=1
                l+=1
        return ans

        