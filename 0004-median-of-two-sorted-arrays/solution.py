class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = total // 2

        low, high = 0, n1

        while low <= high:
            i = (low + high) // 2
            j = half - i

            l1 = nums1[i-1] if i > 0 else float('-inf')
            r1 = nums1[i] if i < n1 else float('inf')
            l2 = nums2[j-1] if j > 0 else float('-inf')
            r2 = nums2[j] if j < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                if total % 2:
                    return min(r1, r2)
                return (max(l1, l2) + min(r1, r2)) / 2

            elif l1 > r2:
                high = i - 1
            else:
                low = i + 1

        