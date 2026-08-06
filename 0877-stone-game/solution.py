class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
         from functools import cache
         @cache
         def solve(left, right):

            # Base case
            if left == right:
                return piles[left]

            # Current player picks left
            pickLeft = piles[left] - solve(left + 1, right)

            # Current player picks right
            pickRight = piles[right] - solve(left, right - 1)

            # Current player chooses the better option
            return max(pickLeft, pickRight)

        # If score difference >= 0, Player 1 can win (or tie)
         return solve(0, len(piles) - 1) >= 0

        