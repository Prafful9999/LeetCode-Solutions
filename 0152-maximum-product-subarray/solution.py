class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        ans=float('-inf')
        n=len(nums)
        for i in range(0,n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix=prefix*nums[i]
            suffix=suffix*nums[n-i-1]
            ans=max(ans,max(prefix,suffix))
        return ans

