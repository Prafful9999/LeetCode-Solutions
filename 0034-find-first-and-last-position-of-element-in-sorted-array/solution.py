class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        low=0
        high=n-1
        l=0
        h=n-1
        lb=-1
        hb=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                if nums[mid]==target:
                  lb=mid
                high=mid-1
            else:
                low=mid+1
        while l<=h:
            m=(l+h)//2
            if nums[m]<=target:
                if nums[m]==target:
                  hb=m
                l=m+1
            else:
                h=m-1
        return [lb,hb]
        