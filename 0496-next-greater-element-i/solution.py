

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            index = nums2.index(i)  # Find the index of i in nums2
            for j in range(index + 1, len(nums2)):
                if nums2[j] > i:
                    ans.append(nums2[j])  # Found next greater element
                    break
            else:
                ans.append(-1)  # No greater element found
        return ans
