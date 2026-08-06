class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums.sort()
        hmap = {}
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        # Special case for 1
        if 1 in count:
            ans = count[1]
            if ans % 2 == 0:
                ans -= 1
        else:
            ans = 1

        for i in range(len(nums)):
            if nums[i] == 1:
                continue

            lst = [nums[i]]
            curr = nums[i]

            while curr * curr in count:
                lst.append(curr * curr)
                curr = curr * curr

            hmap[nums[i]] = lst

        maxi = ans

        for value in hmap.values():
            length = 1

            for i in range(len(value) - 1):
                if count[value[i]] >= 2:
                    length += 2
                else:
                    break

            maxi = max(maxi, length)

        return maxi
        