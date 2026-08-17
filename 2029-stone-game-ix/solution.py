class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        count = [0, 0, 0]

        # Count stones according to remainder
        for stone in stones:
            count[stone % 3] += 1

        def check(count):
            # Alice must start with remainder 1
            if count[1] == 0:
                return False

            count[1] -= 1

            # Number of turns we can continue safely
            turns = 1 + min(count[1], count[2]) * 2

            # Add all remainder-0 stones
            turns += count[0]

            # If extra 1 is available, one more turn is possible
            if count[1] > count[2]:
                count[1] -= 1
                turns += 1

            # Alice wins if:
            # 1. number of turns is odd
            # 2. some stone is still left
            return turns % 2 == 1 and count[1] != count[2]

        # Alice can start with remainder 1
        option1 = check(count.copy())

        # Alice can start with remainder 2
        # Swap the roles of remainder 1 and 2
        swapped = [count[0], count[2], count[1]]
        option2 = check(swapped)

        return option1 or option2