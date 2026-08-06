class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2=len(nums2)
        res=[]
        for i in nums1:
            ind=nums2.index(i)
            found=False
            for j in range(ind+1,n2):
                if nums2[j]>i:
                    res.append(nums2[j])
                    found=True
                    break
            if not found:
                res.append(-1)
        return res
                
