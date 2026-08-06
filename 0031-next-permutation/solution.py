class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def nge(lst,element):
            x=float("inf")
            ind=-1
            for i in range(0,len(lst)):
                if lst[i]>element and lst[i]<x:
                    x=lst[i]
                    ind=i
            return ind
        if nums==sorted(nums,reverse=True):
            nums.reverse()
            return 
        i=len(nums)-2
        while i>=0:
            if nums[i]<nums[i+1]:
                j=i+1
                si=nge(nums[j:],nums[i])
                nums[i],nums[si+j]=nums[si+j],nums[i]
                nums[j:]=sorted(nums[j:])
                break
            i-=1

        


            