class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

            mini=min(nums)
            maxi=max(nums)
            mini_ind=0
            maxi_ind=0
            n=len(nums)
            for i in range(n):
                if nums[i]==mini:
                    mini_ind=i
                if nums[i]==maxi:
                    maxi_ind=i
            if n-abs(maxi_ind-mini_ind)>=k-1:
                return k*(maxi-mini)
            else:
                return k*(maxi-mini)
                    
                    





