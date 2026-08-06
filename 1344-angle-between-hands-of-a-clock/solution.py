class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h_dis=minutes/12
        if hour==12:
            ans=abs(minutes*6-h_dis*6)
        else:
            ans=abs(minutes*6-((hour*5)+h_dis)*6)
        if ans>180:
            return 360-ans
        else:
            return ans
        