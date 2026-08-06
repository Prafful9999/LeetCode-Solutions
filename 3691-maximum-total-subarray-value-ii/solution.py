import heapq
from math import log2

class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)

        LOG = (n).bit_length()

        mx = [nums[:]]
        mn = [nums[:]]

        j = 1
        while (1 << j) <= n:
            prev_max = mx[j - 1]
            prev_min = mn[j - 1]

            cur_max = []
            cur_min = []

            length = 1 << (j - 1)

            for i in range(n - (1 << j) + 1):
                cur_max.append(max(prev_max[i],
                                   prev_max[i + length]))

                cur_min.append(min(prev_min[i],
                                   prev_min[i + length]))

            mx.append(cur_max)
            mn.append(cur_min)
            j += 1

        def value(l, r):
            length = r - l + 1
            p = length.bit_length() - 1

            maximum = max(
                mx[p][l],
                mx[p][r - (1 << p) + 1]
            )

            minimum = min(
                mn[p][l],
                mn[p][r - (1 << p) + 1]
            )

            return maximum - minimum

        heap = []

        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)

            ans += -neg_v

            if r > l:
                nv = value(l, r - 1)
                heapq.heappush(heap, (-nv, l, r - 1))

        return ans