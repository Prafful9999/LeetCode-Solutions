class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums2=[]
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return nums[0]

        def insert(val):
            ind=len(nums2)
            parent_ind=(ind-1)//2
            while ind>0 and nums2[parent_ind]<val:
                if ind==len(nums2):
                    nums2.append(nums2[parent_ind])
                else:
                    nums2[ind]=nums2[parent_ind]
                ind=parent_ind
                parent_ind=(ind-1)//2
            if ind==len(nums2):
                nums2.append(val)
            else:
                nums2[ind]=val

        for i in nums:
            insert(i)

        def delete():
            top_val=nums2[0]
            temp=nums2.pop()
            ind=0
            lc_ind=2*ind+1
            rc_ind=2*ind+2
            while lc_ind<len(nums2):
                if rc_ind<len(nums2):
                    if nums2[lc_ind]>nums2[rc_ind]:
                        if nums2[lc_ind]>temp:
                            nums2[ind]=nums2[lc_ind]
                            ind=lc_ind
                        else:
                            break
                    else:
                        if nums2[rc_ind]>temp:
                            nums2[ind]=nums2[rc_ind]
                            ind=rc_ind
                        else:
                            break
                else:
                    if nums2[lc_ind]>temp:
                        nums2[ind]=nums2[lc_ind]
                        ind=lc_ind
                    else:
                        break
                lc_ind=2*ind+1
                rc_ind=2*ind+2
            nums2[ind]=temp
        for i in range(k-1):
            delete()
        return nums2[0]

                        


