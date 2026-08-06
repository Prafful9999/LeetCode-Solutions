class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[]
        i=0
        j=0
        n=len(nums)
        while j<n:
            if nums[i%n]>nums[j]:
                res.append(nums[i%n])
                j+=1
                i=j+1
            else:
                i+=1
                if i>=2*n:
                    res.append(-1)
                    j+=1
                    i=j+1
                    
                
        return res
                
            

