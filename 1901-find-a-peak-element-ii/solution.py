class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        if len(mat)==1 and len(mat[0])==1:
            return [0,0]
        l=0
        h=len(mat[0])-1
        while l<=h:
            mid=(l+h)//2
            i=0
            r_maxE=-1
            maxE=float('-inf')
            while i<=len(mat)-1:
                if mat[i][mid]>maxE:
                    maxE=mat[i][mid]
                    r_maxE=i
                i+=1
            if mid==0 or mid==len(mat[0])-1:
                if mid==0:
                    if mat[r_maxE][mid]>mat[r_maxE][mid+1]:
                        return [r_maxE,mid]
                    else:
                        l=mid+1
                elif mid==len(mat[0])-1:
                    if mat[r_maxE][mid-1]<mat[r_maxE][mid]:
                        return [r_maxE,mid]
                    else:
                        h=mid-1
            else:
                        
                if mat[r_maxE][mid-1]<mat[r_maxE][mid]>mat[r_maxE][mid+1]:
                    return [r_maxE,mid]
                elif mat[r_maxE][mid-1]>mat[r_maxE][mid]:
                    h=mid-1
                elif mat[r_maxE][mid]<mat[r_maxE][mid+1]:
                    l=mid+1

            
            