class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def palindrome(si,fi):
            while si<=fi:
                if s[si]==s[fi]:
                    si+=1
                    fi-=1
                else:
                    return False
            return True
        def solve(lst,ind):
            if ind==len(s):
                res.append(lst[:])
                return 
            
            for i in range(ind,len(s)):
                x=palindrome(ind,i)
                if x==True:
                    lst.append(s[ind:i+1])
                    solve(lst,i+1)
                    lst.pop()
        solve([],0)
        return res

        
        