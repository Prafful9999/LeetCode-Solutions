class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr=1
        prev=0
        while curr<len(nums):
            if nums[curr]==nums[prev]:
                nums.pop(curr)
                
            else:
                if curr:
                   prev+=1
                   curr+=1
        return len(nums)
        return nums
        