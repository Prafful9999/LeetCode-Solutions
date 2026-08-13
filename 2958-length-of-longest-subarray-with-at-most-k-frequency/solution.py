class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq={}
        i=0
        j=0
        max_len=0
        curr_len=0
        while j<len(nums):
            freq[nums[j]]=freq.get(nums[j],0)+1
            while freq[nums[j]]>k:
                freq[nums[i]]-=1
                i+=1
            curr_len=j-i+1
            max_len=max(max_len,curr_len)
            j+=1
        return max_len
            
            
        