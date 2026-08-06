class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        for i in s:
            if i in t:
                t.remove(i)
                
            else:
                return False
        if len(t)==0:
            return True
        return False