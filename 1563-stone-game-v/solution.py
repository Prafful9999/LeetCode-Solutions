class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        n = len(stoneValue)

        # prefix[i] = first i stones ka sum
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[-1] * n for _ in range(n)]

        def solver(i, j):

            # sirf ek stone hai -> split nahi kar sakte
            if i == j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0

            # k ke left me [i...k]
            # right me [k+1...j]
            for k in range(i, j):

                left = prefix[k + 1] - prefix[i]
                right = prefix[j + 1] - prefix[k + 1]

                if left < right:
                    # left part choose kar sakte hain
                    ans = max(ans, left + solver(i, k))

                elif right < left:
                    # right part choose kar sakte hain
                    ans = max(ans, right + solver(k + 1, j))

                else:
                    # equal hain -> dono me se choose kar sakte hain
                    ans = max(
                        ans,
                        left + solver(i, k),
                        right + solver(k + 1, j)
                    )

            dp[i][j] = ans
            return ans

        return solver(0, n - 1)