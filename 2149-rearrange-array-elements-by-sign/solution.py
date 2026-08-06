class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        res=[]
        for i in nums:
            if i>0:
                positive.append(i)
            else:
                negative.append(i)
        i=0
        j=0
        for nums in positive:
            res.append(positive[i])
            res.append(negative[j])
            i+=1
            j+=1
        return res


        