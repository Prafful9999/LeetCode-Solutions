class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxi=max(costs)
        arr=[0 for i in range(maxi+1)]
        for i in costs:
            arr[i]+=1
        j=0
        k=0
        while j<maxi+1:
            while arr[j]!=0:
                costs[k]=j
                arr[j]-=1
                k+=1
            j+=1
        print(costs)


        
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


