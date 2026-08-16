class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        non_zero=False
        xor=0
        for i in range(len(nums)):
            xor=xor^nums[i]
            if xor!=0:
              non_zero=True
        if xor!=0:
            return len(nums)
        if non_zero:
            return len(nums)-1
        return 0
    
        