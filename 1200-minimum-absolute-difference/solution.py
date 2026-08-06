class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff=float("inf")
        for i in range(len(arr)):
            if i>0:
                diff=arr[i]-arr[i-1]
                min_diff=min(min_diff,diff)
        ans=[]
        for i in range(len(arr)):
            if i>0:
                if arr[i]-arr[i-1]==min_diff:
                    ans.append([arr[i-1],arr[i]])
        return ans
        
        