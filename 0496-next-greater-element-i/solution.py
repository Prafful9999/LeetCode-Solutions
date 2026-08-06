class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        # Step 1: Build next greater map using nums2
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        
        # Step 2: Remaining elements in stack have no next greater
        for num in stack:
            next_greater[num] = -1
        
        # Step 3: Manually build the result for nums1
        result = []
        for num in nums1:
            if num in next_greater:
                result.append(next_greater[num])
            else:
                result.append(-1)  # Just in case (though shouldn't happen in valid inputs)

        return result
