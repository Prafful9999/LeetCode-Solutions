class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        lst=[]
        for i in range(len(nums)):
            if nums[i]==0:
                lst.append(count)
                count=0
            else:
                count+=1
        lst.append(count)

        return max(lst)
            


        