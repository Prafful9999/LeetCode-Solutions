class Solution:
    def check(self, nums: List[int]) -> bool:
        sortednums=sorted(nums)
        newnums=sortednums+sortednums
        for i in range(len(nums)):
            if newnums[i:i+len(nums)]==nums:
                return True
        return False
        