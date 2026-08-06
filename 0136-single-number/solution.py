class Solution:
    def singleNumber(self, nums: List[int]) -> int:

            
            n=len(nums)
            hash={}
            for i in range(n):
                if nums[i] not in hash:
                    hash[nums[i]]=1
                else:
                    hash[nums[i]]+=1
            for k,v in hash.items():
                if v==1:
                    return k

                    