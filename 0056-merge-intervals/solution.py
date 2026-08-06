class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        n=len(intervals)
        mini=intervals[0][0]
        maxi=intervals[0][1]
        if n==1:
            return [intervals[0]]
        for i in range(1,n):
            if intervals[i][0]<=maxi:
                mini=min(mini,intervals[i][0])
                maxi=max(maxi,intervals[i][1])
                
            elif intervals[i][0]>maxi:
                res.append([mini,maxi])
                mini=intervals[i][0]
                maxi=intervals[i][1]
                
        res.append([mini,maxi])
        return res
            



