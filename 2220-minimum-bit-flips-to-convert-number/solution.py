class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal
        count = 0
        while x > 0:
            count += x & 1
            x >>= 1
        return count
