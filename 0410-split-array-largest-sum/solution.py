class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            count=0
            total=0
            for i in nums:
                total+=i
                if total>mid:
                    count+=1
                    total=i
            if total<=mid:
                count+=1
            if count>k:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans