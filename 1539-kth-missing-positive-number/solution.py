class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        x=arr[-1]+k
        new_arr=[]
        for i in range(1,x+1):
            if i not in arr:
                new_arr.append(i)
        low=0
        high=len(new_arr)-1
        while low<=high:
            mid=(low+high)//2
            if mid==k-1:
                return new_arr[mid]
            elif mid<k-1:
                low=mid+1
            else:
                high=mid-1
        
