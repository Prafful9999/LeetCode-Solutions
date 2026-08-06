class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        htable={}
        for i in nums:
            if i not in htable:
                htable[i]=1
            else:
                htable[i]+=1
        for i in htable:
            if htable[i]==1:
                return i

        
        