class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum=sum(nums)
        psum=0
        x=-1
        for i in range(0,len(nums)):
            rsum=totalsum-(psum+nums[i])
            if rsum==psum:
                x=i
                break
            else:
                psum+=nums[i]
        return x

        