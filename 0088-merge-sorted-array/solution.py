class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j,k=0,0,0
        unums1=nums1[:m]
        while i<m and j<n:
                if unums1[i]<=nums2[j]:
                        nums1[k]=unums1[i]
                        i+=1
                else:
                        nums1[k]=nums2[j]
                        j+=1
                k+=1
        while i<m:
            nums1[k]=unums1[i]
            k+=1
            i+=1
        while j<n:
            nums1[k]=nums2[j]
            k+=1
            j+=1
        


        
