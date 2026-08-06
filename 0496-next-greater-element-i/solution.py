class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap={nums2[-1]:-1}
        stack=[nums2[-1]]
        n2=len(nums2)
        for i in range(n2-2,-1,-1):
            if nums2[i]>stack[-1]:
                while stack and nums2[i]>stack[-1]:
                    stack.pop()
                if len(stack)==0:
                    hmap[nums2[i]]=-1
                else:
                    hmap[nums2[i]]=stack[-1]
                stack.append(nums2[i])
            else:
                hmap[nums2[i]]=stack[-1]
                stack.append(nums2[i])
        res=[]
        for i in nums1:
            res.append(hmap[i])
        return res

            