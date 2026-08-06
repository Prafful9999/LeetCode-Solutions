class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ind=0
        for j in range(len(nums)):
            if nums[j]==pivot:
                ind=j
                break
        small=[]
        large=[]
        equal=[]
        for i in range(len(nums)):
            if i==ind:
                continue
            if nums[i]<nums[ind]:
                small.append(nums[i])
            elif nums[i]==nums[ind]:
                 equal.append(nums[i])
            else:
                large.append(nums[i])
        print(small)
        print(large)
        nums=small+equal+[pivot]+large
        return nums


        