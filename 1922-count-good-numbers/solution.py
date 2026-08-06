class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def recursive_power(base, exponent, modulus):
            if exponent == 0:
                return 1
            half = recursive_power(base, exponent // 2, modulus)
            half = (half * half) % modulus
            if exponent % 2 == 1:
                half = (half * base) % modulus
            return half
        even_count = (n + 1) // 2
        odd_count = n // 2
        even_part = recursive_power(5, even_count, MOD)
        odd_part = recursive_power(4, odd_count, MOD)
        return (even_part * odd_part) % MOD

        