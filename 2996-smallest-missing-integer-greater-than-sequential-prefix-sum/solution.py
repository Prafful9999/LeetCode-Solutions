class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]+1

        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        i=0
        j=1
        total=nums[i]
        while j<len(nums) and nums[j]-nums[i]==1:
            total+=nums[j]
            j+=1
            i+=1
        while total in dic:
            total+=1
        return total


