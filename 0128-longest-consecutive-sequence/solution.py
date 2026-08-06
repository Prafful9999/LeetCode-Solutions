class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==None:
            return 0
        new_set=set(nums)
        longest=0
        for i in new_set:
            if i-1 not in new_set:
                length=1
                count=i
                while count+1 in new_set:
                    length+=1
                    count+=1
                longest=max(longest,length)
        return longest
