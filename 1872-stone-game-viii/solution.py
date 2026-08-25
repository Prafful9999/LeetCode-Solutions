class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # prefix sum
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        dp = [0] * n

        # Last possible state
        dp[n - 1] = prefix[n - 1]

        for i in range(n - 2, 0, -1):
            dp[i] = max(prefix[i] - dp[i + 1], dp[i + 1])

        return dp[1]