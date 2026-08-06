class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        from functools import lru_cache

        def solve(n):

            s = str(n)

            @lru_cache(None)
            def dp(pos, tight, started, prev2, prev1):

                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_count = 0
                total_waviness = 0

                for d in range(limit + 1):

                    new_tight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            new_tight,
                            False,
                            10,
                            10
                        )

                        total_count += cnt
                        total_waviness += wav

                    else:

                        if not started:
                            cnt, wav = dp(
                                pos + 1,
                                new_tight,
                                True,
                                10,
                                d
                            )

                            total_count += cnt
                            total_waviness += wav

                        else:

                            add = 0

                            if prev2 != 10:
                                if (prev1 > prev2 and prev1 > d) or \
                                   (prev1 < prev2 and prev1 < d):
                                    add = 1

                            cnt, wav = dp(
                                pos + 1,
                                new_tight,
                                True,
                                prev1,
                                d
                            )

                            total_count += cnt
                            total_waviness += wav + add * cnt

                return (total_count, total_waviness)

            return dp(0, True, False, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)
        