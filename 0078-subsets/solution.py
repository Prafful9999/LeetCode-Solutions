class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        def solve(ind,lst):
            if ind==len(nums):
                return
            for i in range(ind,len(nums)):
                lst.append(nums[i])
                res.append(lst[:])
                solve(i+1,lst)
                lst.pop()
        solve(0,[])
        return res
