class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        # Row number -> reserved seats
        rows = {}

        for r, c in reservedSeats:
            if r not in rows:
                rows[r] = set()
            rows[r].add(c)

        # Initially every row can fit 2 families
        ans = (n - len(rows)) * 2

        # Check only rows having reserved seats
        for r in rows:

            seats = rows[r]

            left = True
            middle = True
            right = True

            # Family: 2,3,4,5
            for seat in [2, 3, 4, 5]:
                if seat in seats:
                    left = False

            # Family: 4,5,6,7
            for seat in [4, 5, 6, 7]:
                if seat in seats:
                    middle = False

            # Family: 6,7,8,9
            for seat in [6, 7, 8, 9]:
                if seat in seats:
                    right = False

            if left and right:
                ans += 2

            elif left or middle or right:
                ans += 1

        return ans