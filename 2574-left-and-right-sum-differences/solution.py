class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[]
        rightsum=[]
        answer=[]
        n=len(nums)
        total_sum=sum(nums)
        total=0
        for i in range(n):
            element=total
            leftsum.append(total)
            total+=nums[i]
            rightsum.append(total_sum-total)
            answer.append(abs(element-(total_sum-total)))
        return answer
        
        


        