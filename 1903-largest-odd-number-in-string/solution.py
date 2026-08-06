class Solution:
    def largestOddNumber(self, num: str) -> str:
        ind=-1
        for i in range(0,len(num)):
            if int(num[i])%2!=0:
                ind=i
        if ind==-1:
            return ""
        if ind==len(num)-1:
            return num
        return num[:ind+1]
