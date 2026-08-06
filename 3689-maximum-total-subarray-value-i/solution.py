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
            return k*(maxi-mini)
                    





