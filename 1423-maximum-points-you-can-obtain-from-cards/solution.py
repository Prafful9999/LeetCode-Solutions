class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=0
        n=len(cardPoints)
        total=0
        minsum=float('inf')
        if k==n:
            return sum(cardPoints)
        for r in range(0,n):
            total+=cardPoints[r]
            if r-l+1==n-k:
                minsum=min(minsum,total)
                total-=cardPoints[l]
                l+=1
        return sum(cardPoints)-minsum


        
