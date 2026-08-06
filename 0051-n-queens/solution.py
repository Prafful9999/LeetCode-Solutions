class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        lst=[]
        st="."*n
        for i in range(n):
            lst.append(st)
        def issolve(row,col,lst,n):
            ccol=col
            while ccol>=0:
                if lst[row][ccol]=="Q":
                    return False
                ccol-=1
            urow=row
            ucol=col
            while urow>=0 and ucol>=0:
                if lst[urow][ucol]=="Q":
                    return False
                urow-=1
                ucol-=1
            drow=row
            dcol=col
            while drow<n and dcol>=0:
                if lst[drow][dcol]=="Q":
                    return False
                drow+=1
                dcol-=1
            return True

            

        def helper(col,res,lst,n):
            if col==n:
                res.append(list(lst))
                return 
            for row in range(n):
                if issolve(row,col,lst,n):
                    lst[row]=lst[row][:col]+"Q"+lst[row][col+1:]
                    helper(col+1,res,lst,n)
                    lst[row]=lst[row][:col]+"."+lst[row][col+1:]
        helper(0,res,lst,n)
        return res
                    