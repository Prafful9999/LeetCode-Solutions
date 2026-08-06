class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            total=0
            for i in nums:
                total+=ceil(i/mid)
            if total>threshold:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans

            
        