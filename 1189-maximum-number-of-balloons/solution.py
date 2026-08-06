class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap={'b':0,'a':0,'l':0,'o':0,'n':0}
        for i in text:
            if i=='b':
                hmap[i]+=1
            if i=='a':
                hmap[i]+=1
            if i=='l':
                hmap[i]+=1
            if i=='o':
                hmap[i]+=1
            if i=='n':
                hmap[i]+=1
        hmap['l']=hmap['l']//2
        hmap['o']=hmap['o']//2
        lst=list(hmap.values())
        mini=min(lst)
        return mini
        