class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        n=len(intervals)
        
        maxi=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]<maxi:
                count+=1
                maxi=min(maxi,intervals[i][1])
            else:
               maxi=max(maxi,intervals[i][1])
        return count
            

        