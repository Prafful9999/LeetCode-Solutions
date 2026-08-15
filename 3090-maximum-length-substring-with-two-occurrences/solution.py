class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        dic={}
        i=0
        j=0
        length=0
        max_length=0
        while j<len(s):
            if s[j] in dic:
                dic[s[j]]+=1
            else:
                dic[s[j]]=1
            length+=1
            while dic[s[j]]>2:
                if s[i] in dic:
                    dic[s[i]]-=1
                else:
                    dic[s[i]]=1
                i+=1
                length=j-i+1
            max_length=max(length,max_length)
            j+=1
        return max_length
