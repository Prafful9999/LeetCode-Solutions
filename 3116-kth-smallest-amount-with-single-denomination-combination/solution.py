class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a // gcd(a, b)) * b

        # x tak kitne unique amounts ban sakte hain
        def count(x):
            ans = 0

            # saare subsets check karenge
            for mask in range(1, 1 << n):

                L = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        L = lcm(L, coins[i])
                        bits += 1

                        if L > x:
                            break

                if L > x:
                    continue

                # odd subset -> add
                # even subset -> subtract
                if bits % 2 == 1:
                    ans += x // L
                else:
                    ans -= x // L

            return ans

        # Binary Search
        left = 1
        right = k * min(coins)

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left