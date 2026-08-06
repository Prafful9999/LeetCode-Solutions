class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        lfar=0
        lnear=0
        count=defaultdict(int)
        ans=0
        for i in range(len(nums)):
            count[nums[i]]+=1
            while len(count)>k:
                 count[nums[lnear]]-=1
                 if count[nums[lnear]]==0:
                    count.pop(nums[lnear])
                 lnear+=1
                 lfar=lnear
            while count[nums[lnear]]>1:
                count[nums[lnear]]-=1
                lnear+=1

            if len(count)==k:
                ans+=lnear-lfar+1
        return ans
