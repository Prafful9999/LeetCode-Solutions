class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        left=[-1]*n
        for i in range(n):
            if i==0:
                left[0]=1
            else:
                if ratings[i]>ratings[i-1]:
                    left[i]=left[i-1]+1
                else:
                    left[i]=1
        right=[-1]*n
        total=0
        for j in range(n-1,-1,-1):
            if j==n-1:
                right[j]=1
                total+=max(1,left[j])
            else:
                if ratings[j]>ratings[j+1]:
                    right[j]=right[j+1]+1
                    total+=max(right[j],left[j])
                else:
                    right[j]=1
                    total+=max(right[j],left[j])
        
        print(left)
        print(right)
        return total


            

        