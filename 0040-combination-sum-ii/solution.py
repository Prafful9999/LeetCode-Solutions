class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def solve(ind,total,lst):
            if total==target:
                res.append(lst[:])
                return 
            if total>target or ind==len(candidates):
                return 
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue 
                lst.append(candidates[i])
                solve(i+1,total+candidates[i],lst)
                lst.pop()
        solve(0,0,[])
        return res
            