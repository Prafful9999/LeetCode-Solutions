class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=0
        while low<=high:
            mid=(low+high)//2
            total=0
            for i in piles:
                total+=ceil(i/mid)
            if total>h:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans

        

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         