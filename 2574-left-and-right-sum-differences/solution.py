class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer=[]
        n=len(nums)
        total_sum=sum(nums)
        total=0
        for i in range(n):
            element=total
            total+=nums[i]
            answer.append(abs(element-(total_sum-total)))
        return answer
        
        


        