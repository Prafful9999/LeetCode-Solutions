class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        low=0
        high=row*col-1
        while low<=high:
            mid=(low+high)//2
            n_row=mid//col
            n_col=mid%col
            if matrix[n_row][n_col]==target:
                return True
            elif matrix[n_row][n_col]<target:
                low=mid+1
            else:
                high=mid-1
        return False