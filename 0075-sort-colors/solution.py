class Solution:
    def sortColors(self, nums: List[int]) -> None:
        dict1={}
        dict1[0]=0
        dict1[1]=0
        dict1[2]=0
        for i in nums:
            if i==0:
                dict1[0]+=1
            elif i==1:
                dict1[1]+=1
            else:
                dict1[2]+=1
        for i in range(0,dict1[0]):
            nums[i]=0
        for i in range(dict1[0],dict1[0]+dict1[1]):
            nums[i]=1
        for i in range(dict1[1]+dict1[0],len(nums)):
            nums[i]=2
        

    
        