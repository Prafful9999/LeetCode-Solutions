class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        n=len(nums)
        high=n-1
        min_val=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                min_val=min(min_val,nums[low])
                low=mid+1
            else:
                min_val=min(min_val,nums[mid])
                high=mid-1
        return min_val
        