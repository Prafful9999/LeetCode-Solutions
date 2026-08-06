class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
       n=len(s)
       right=0
       left=0
       count=0
       lst=[0]*3
       while True:
        
        while lst[0]>0 and lst[1]>0 and lst[2]>0:
            count+=n-right+1
            lst[ord(s[left])-ord('a')]-=1
            left+=1
        if right>=n:
            return count
        else:
            lst[ord(s[right])-ord('a')]+=1
            right+=1
       
        
        
        

