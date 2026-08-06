class Solution:
    def predictTheWinner(self, nums):

        def solve(left, right):

            # Base case
            if left == right:
                return nums[left]

            # Current player picks left
            pickLeft = nums[left] - solve(left + 1, right)

            # Current player picks right
            pickRight = nums[right] - solve(left, right - 1)

            # Current player chooses the better option
            return max(pickLeft, pickRight)

        # If score difference >= 0, Player 1 can win (or tie)
        return solve(0, len(nums) - 1) >= 0