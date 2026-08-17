class Solution:
    def rob(self, nums: List[int]) -> int:
        maxi=float('-inf')
        dp=[-1]*len(nums)
        def solver(ind):
            if ind==0:
                return nums[0]
            if ind==1:
                return max(nums[1],nums[0])
            if dp[ind]!=-1:
                return dp[ind]
            dp[ind]=max(solver(ind-2)+nums[ind],solver(ind-1))
            return dp[ind]
        return solver(len(nums)-1)


        