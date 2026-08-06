class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        htableST={}
        htableTS={}
        for i in range(0,len(s)):
            if s[i]  not in htableST:
                htableST[s[i]]=t[i]
        for i in range(0,len(t)):
            if t[i]  not in htableTS:
                htableTS[t[i]]=s[i]
        for i,j in zip(s,t):
            if htableST[i]!=j or htableTS[j]!=i:
                return False
        return True

        