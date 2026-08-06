class Solution:
    def romanToInt(self, s: str) -> int:
        htable={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=0
        i=0
        while i<len(s):
             if i+1<len(s) and s[i]+s[i+1] in ["IV" , "IX" , "XL" , "XC" , "CD" , "CM"]:
                total+=htable[s[i+1]]-htable[s[i]]
                i+=2
             else:
                total+=htable[s[i]]
                i+=1
        return total



        