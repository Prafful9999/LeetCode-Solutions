class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        i=0
        n=len(costs)
        while coins>0 and i<len(costs):
            coins-=costs[i]
            if coins<0:
                return count
            count+=1
            i+=1
        return count


