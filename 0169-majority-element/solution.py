class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        
        for k,v in dict1.items():
            if v>len(nums)/2:
                return k
        
        