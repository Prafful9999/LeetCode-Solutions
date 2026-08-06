class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
       g.sort()
       s.sort()
       i=0
       j=0
       n1=len(g)
       n2=len(s)
       count=0
       while i<n1 and j<n2:
        if s[j]>=g[i]:
            j+=1
            i+=1
            count+=1
        else:
            j+=1
       return count
      