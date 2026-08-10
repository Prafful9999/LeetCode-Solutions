class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix sum
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        from functools import lru_cache

        @lru_cache(None)
        def solve(i, M):
            if i >= n:
                return 0

            # If we can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            ans = 0

            # Take X piles, where 1 <= X <= 2*M
            for X in range(1, 2 * M + 1):
                # Current player gets:
                # total remaining - opponent's maximum
                opponent = solve(i + X, max(M, X))
                ans = max(ans, suffix[i] - opponent)

            return ans

        return solve(0, 1)