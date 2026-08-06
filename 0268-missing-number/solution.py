class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            correct = nums[i]
            # place number only if it is within range [0, n-1]
            if correct < n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        # find first index where value doesn't match
        for i in range(n):
            if nums[i] != i:
                return i

        # if all match, missing number is n
        return n
  