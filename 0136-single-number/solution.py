class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i in freq.keys():
                freq[i] +=1
            else:
                freq[i] = 1
        for key in freq.keys():
            if freq[key] == 1:
                return key
        