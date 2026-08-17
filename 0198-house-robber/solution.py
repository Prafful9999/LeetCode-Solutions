class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        prev2=nums[0]
        prev1=max(nums[0],nums[1])
        for ind in range(2,len(nums)):
            curr=max(prev2+nums[ind],prev1)
            prev2=prev1
            prev1=curr
        return prev1
        
        '''
        maxi=float('-inf')
        if len(nums)==1:
            return nums[0]
        dp=[-1]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for ind in range(2,len(nums)):
            dp[ind]=max(dp[ind-2]+nums[ind],dp[ind-1])
        return dp[-1]
    

        def solver(ind):
            if ind==0:
                return nums[0]
            if ind==1:
                return max(nums[1],nums[0])
            if dp[ind]!=-1:
                return dp[ind]
            dp[ind]=max(solver(ind-2)+nums[ind],solver(ind-1))
            return dp[ind]
        return solver(len(nums)-1)'''


        