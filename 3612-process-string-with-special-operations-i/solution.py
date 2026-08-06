class Solution:
    def processStr(self, s: str) -> str:
        res=''
        for i in s:
            if i!='#' and i!='*' and i!='%':
                res+=i
                curr=res
            elif i=='*':
                if len(res)!=0:
                    res=res[:-1]
            elif i=='#':
                res+=res
            elif i=='%':
                if len(res)!=0:
                    res=res[::-1]
        return res
        
            
            


        