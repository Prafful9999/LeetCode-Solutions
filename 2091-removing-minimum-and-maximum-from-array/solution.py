class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        mini=float('inf')
        maxi=float('-inf')
        mini_ind=-1
        maxi_ind=-1
        for i in range(n):
            if nums[i]<mini:
                mini=nums[i]
                mini_ind=i
            if nums[i]>maxi:
                maxi=nums[i]
                maxi_ind=i
        lesser_ind=min(maxi_ind,mini_ind)
        greater_ind=max(maxi_ind,mini_ind)
        last=n-greater_ind
        if lesser_ind+1<last:
            d1=lesser_ind+1
            d2=min(greater_ind-lesser_ind,last)
            return d1+d2
        else:
            d1=last
            d2=min(lesser_ind+1,greater_ind-lesser_ind)
            return d1+d2