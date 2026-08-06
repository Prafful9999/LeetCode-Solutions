class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[]
        stack=[nums[-1]]
        n=len(nums)
        for i in range(2*n-2,-1,-1):
            
            if nums[i%n]>=stack[-1]:
                while stack and stack[-1]<=nums[i%n]:
                    stack.pop()
                if i<n:
                    if len(stack)==0:
                        res.append(-1)
                    else:
                        res.append(stack[-1])
                stack.append(nums[i%n])
            else:
                if i<n:
                    res.append(stack[-1])
                stack.append(nums[i%n])
        return res[::-1]
        

        
