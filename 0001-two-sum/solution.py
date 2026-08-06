class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            com=target-nums[i]
            if com in dict1.keys():
                return [i,dict1[com]]
            else:
                dict1[nums[i]]=i


        