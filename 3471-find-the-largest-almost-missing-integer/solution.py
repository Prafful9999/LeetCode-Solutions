class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        from collections import Counter
        def detect(nums):
            if len(nums)==1:
                return True
            for i in range(1,len(nums)):
                if nums[i]!=nums[i-1]:
                    return False
            return True
        freq=Counter(nums)
        if k==len(nums):
            return max(nums)
        val=detect(nums)
        if not val and k==1:
            ans=-1
            for i in range(len(nums)):
                if freq[nums[i]]==1:
                     ans=max(ans,nums[i])
            return ans

        ans=-1
        if freq[nums[0]]==1:
            ans=max(ans,nums[0])
        if freq[nums[-1]]==1:
            ans=max(ans,nums[-1])
        return ans

        