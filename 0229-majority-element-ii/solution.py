class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict1={}
        res=[]
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for key,val in dict1.items():
            if val>(len(nums)/3):
                res.append(key)
        return res

        


        