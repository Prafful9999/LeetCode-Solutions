class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def solve(ind,total,lst):
            if total==n and len(lst)==k:
                res.append(lst[:])
                return 
            if total>n:
                return
            if len(lst)>k:
                return 
            for i in range(ind,10):
                lst.append(i)
                solve(i+1,total+i,lst)
                lst.pop()
        solve(1,0,[])
        return res


        