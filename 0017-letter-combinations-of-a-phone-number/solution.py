class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        def solve(ind,dstr):
            if ind==len(digits):
                res.append(dstr)
                return 
            for i in dic[digits[ind]]:
                solve(ind+1,dstr+i)
        solve(0,"")
        return res
        