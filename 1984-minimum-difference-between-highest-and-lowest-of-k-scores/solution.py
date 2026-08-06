class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=float("inf")
        n=len(nums)
        i=0
        j=0
        while j<n:
            if j-i+1==k:
                diff=nums[j]-nums[i]
                ans=min(ans,diff)
                i+=1
                j=i
            j+=1
        return ans