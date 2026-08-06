class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hmap={5:0,10:0,20:0}
        hmap[bills[0]]+=1
        if len(bills)==1:
            if hmap[5]==1:
                return True
            else:
                return False
        else:
            for i in range(1,len(bills)):
                if bills[i]==5:
                    hmap[bills[i]]+=1
                elif bills[i]==10:
                    hmap[10]+=1
                    if hmap[5]>0:
                       hmap[5]-=1
                    else:
                        return False
                elif bills[i]==20:
                    hmap[20]+=1
                    if hmap[10]>0 and hmap[5]==0:
                        return False
                    elif hmap[10]>0 and hmap[5]>0:
                        hmap[10]-=1
                        hmap[5]-=1
                    elif hmap[10]==0 and hmap[5]>=3:
                        hmap[5]-=3
                    else:
                        return False


        
        return True
            

            