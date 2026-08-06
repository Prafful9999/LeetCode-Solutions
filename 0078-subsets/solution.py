class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def solve(ind,lst):
            if ind==len(nums):
                res.append(lst[:])
                return
            lst.append(nums[ind])
            solve(ind+1,lst)
            lst.pop()
            solve(ind+1,lst)

        solve(0,[])
        return res
