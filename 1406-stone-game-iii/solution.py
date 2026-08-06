from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)

        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0

            take = 0
            best = float("-inf")

            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    best = max(best, take - dfs(i + k + 1))

            return best

        score = dfs(0)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"
        