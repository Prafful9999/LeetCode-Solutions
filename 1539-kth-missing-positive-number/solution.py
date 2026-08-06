class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        x=arr[-1]+k
        new_arr=[]
        count=0
        for i in range(1,x+1):
            if i not in arr:
                new_arr.append(i)
                count+=1
                if count==k:
                    return i
        