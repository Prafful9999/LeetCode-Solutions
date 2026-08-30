class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        arr = sorted((x, i) for i, x in enumerate(nums))

        i = 0

        while i < n:
            j = i

            # Same group mein elements ka difference <= limit hona chahiye
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Is group ke values ko sorted order mein
            # original positions par daal do
            positions = sorted(arr[k][1] for k in range(i, j + 1))

            for k, pos in enumerate(positions):
                nums[pos] = arr[i + k][0]

            i = j + 1

        return nums