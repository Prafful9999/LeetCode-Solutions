class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def solve(firstStart, firstDur, secondStart, secondDur):

            second = sorted(zip(secondStart, secondDur))
            m = len(second)

            starts = [s for s, d in second]

            prefixMinDur = [0] * m
            prefixMinDur[0] = second[0][1]

            for i in range(1, m):
                prefixMinDur[i] = min(prefixMinDur[i - 1], second[i][1])

            suffixMinFinish = [0] * m
            suffixMinFinish[m - 1] = second[m - 1][0] + second[m - 1][1]

            for i in range(m - 2, -1, -1):
                suffixMinFinish[i] = min(
                    suffixMinFinish[i + 1],
                    second[i][0] + second[i][1]
                )

            ans = float("inf")

            for s, d in zip(firstStart, firstDur):

                t = s + d

                low, high = 0, m - 1
                k = -1

                while low <= high:
                    mid = (low + high) // 2

                    if starts[mid] <= t:
                        k = mid
                        low = mid + 1
                    else:
                        high = mid - 1

                if k >= 0:
                    ans = min(ans, t + prefixMinDur[k])

                if k + 1 < m:
                    ans = min(ans, suffixMinFinish[k + 1])

            return ans

        return min(
            solve(
                landStartTime,
                landDuration,
                waterStartTime,
                waterDuration
            ),
            solve(
                waterStartTime,
                waterDuration,
                landStartTime,
                landDuration
            )
        )
        