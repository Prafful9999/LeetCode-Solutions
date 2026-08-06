class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        min_cost=0
        n=len(cost)
        j=0
        for i in cost:
            if j!=2:
               min_cost+=i
               j+=1
            else:
                j=0
        return min_cost
        
            



        