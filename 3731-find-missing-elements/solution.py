class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        new_set=set()
        for i in range(min(nums),max(nums)+1):
            new_set.add(i)
        for j in nums:
            new_set.remove(j)
        return sorted(list(new_set))


        