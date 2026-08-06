class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=0
        while low<=high:
            mid=(low+high)//2
            total=0
            count=0
            for i in weights:
                total+=i
                if total==mid:
                    count+=1
                    total=0
                elif total>mid:
                    count+=1
                    total=i
            
            if total!=0:
                count+=1
            if count>days:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans
                