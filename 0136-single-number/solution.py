class Solution:
    def singleNumber(self, nums: List[int]) -> int:

            
            n=len(nums)
            c=nums[0]

            for i in range(1,n):
                c=c^nums[i]
            return c
                
                