class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i=0
        j=0
        n=len(s)
        count=0
        mini=float('inf')
        mini_ind=-1
        max_ind=-1
        while j<n and i<n:
            if s[j]=='1':
                count+=1
            while count==k:
                clen=j-i+1
                if clen<mini:
                    mini_ind=i
                    max_ind=j
                    mini=clen
                elif clen == mini:
                    if s[i:j+1] < s[mini_ind:max_ind+1]:
                        mini_ind = i
                        max_ind = j
                if s[i]=='1':
                    count-=1
                i+=1
            j+=1
        return s[mini_ind:max_ind+1]
                
                

            
            
       