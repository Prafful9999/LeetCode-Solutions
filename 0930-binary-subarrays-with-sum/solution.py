class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(K):
            if K < 0:
                return 0

            l = 0
            s = 0
            count = 0

            for r in range(len(nums)):
                s += nums[r]

                while s > K:
                    s -= nums[l]
                    l += 1

                count += (r - l + 1)

            return count
        return atMost(goal) - atMost(goal-1)
