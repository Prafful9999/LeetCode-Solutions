class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low=1
        high=max(bloomDay)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            i=0
            j=0
            count=0
            x=0
            while j<len(bloomDay):
                if mid>=bloomDay[j]:
                    count+=1
                    if count==k:
                        x+=1
                        count=0
                        i=j+1
                    j+=1
                else:
                    i+=1
                    j+=1
                    count=0
                    
            if x>=m:
                ans=mid
                high=mid-1

            else: 
               low=mid+1
        return ans

        