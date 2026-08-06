class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        csum = 0
        ans = 0
        htable = {0: 1}  

        for i in nums:
            csum += i

            if csum - k in htable:
                ans += htable[csum - k]

            htable[csum] = htable.get(csum, 0) + 1

        return ans
