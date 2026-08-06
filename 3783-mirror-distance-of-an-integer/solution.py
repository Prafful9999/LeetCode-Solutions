class Solution:
    def mirrorDistance(self, n: int) -> int:
        def rev(n):
            s=str(n)
            rs=s[::-1]
            return int(rs)
        return abs(n-rev(n))
        