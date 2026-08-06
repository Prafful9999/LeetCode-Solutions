class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target==i[0] or target==i[-1]:
                    return True
            if i[0]<target and target<i[-1]:
                low=0
                high=len(i)-1
                while low<=high:
                    mid=(low+high)//2
                    if i[mid]==target:
                        return True
                    elif i[mid]<target:
                        low=mid+1
                    else:
                        high=mid-1
        return False
            
