class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
            count=0
            for i in range(0,len(nums)):
                if nums[i]==0:
                    count+=1

            if count>0:
                pos=nums.index(0)

                for i in range(pos+1,len(nums)):
                    if nums[i]!=0:
                        nums[pos],nums[i]=nums[i],nums[pos]
                        pos+=1
