class Solution:
    def processStr(self, s: str) -> str:
        res=[]
        for i in s:
            if i!='#' and i!='*' and i!='%':
                res.append(i)
            elif i=='*':
                if len(res)!=0:
                    res.pop()
            elif i=='#':
                res.extend(res)
            elif i=='%':
                if len(res)!=0:
                    res.reverse()
        return ''.join(res)
        
            
            


        