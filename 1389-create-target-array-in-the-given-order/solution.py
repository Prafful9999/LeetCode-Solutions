class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        TargetArray=[]
        for i,j in zip(index,nums):
            TargetArray.insert(i,j)
        return TargetArray
            

        