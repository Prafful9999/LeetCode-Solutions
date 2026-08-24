class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        lsum=0
        rsum=0
        lq=0
        rq=0
        for i in range(n//2):
            if num[i]=='?':
                lq+=1
            else:
                lsum+=int(num[i])
        for i in range(n//2,n):
            if num[i]=='?':
                rq+=1
            else:
                rsum+=int(num[i])
        sdiff=(lsum-rsum)
        qdiff=(lq-rq)
        print(qdiff)
        
        if qdiff==0:
            if sdiff==0:
                return False
            else:
                return True
        elif qdiff%2!=0:
            return True
        elif qdiff%2==0:
            max_psum=9*(qdiff//2)
            if (-max_psum)==sdiff:
                return False
            else:
                return True
        
        