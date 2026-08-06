class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def solve(ind,lst):
            res.append(lst[:]) 
            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue   
                lst.append(nums[i])
                solve(i+1,lst)
                lst.pop()
        solve(0,[])
        return res
                
            