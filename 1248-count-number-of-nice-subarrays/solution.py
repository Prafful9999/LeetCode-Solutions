class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(goal):
            if goal<0:
                return 0
            l=0
            codd=0
            count=0
            r=0
            for r in range(len(nums)):
                if nums[r]%2==1:
                    codd+=1
                
                
                while codd>goal:
                    if nums[l]%2==1:
                        codd-=1
                        
                    l+=1
                count+=(r-l+1)
                
            return count
        return atmost(k)-atmost(k-1)
            

        