class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(num):
            lst=list(str(num))
            i=0
            j=1
            k=2
            n=len(lst)
            if n==2 or n==1:
                return 0
            count=0
            while k!=n:
                a=int(lst[j])>int(lst[i]) and int(lst[j])>int(lst[k])
                b= int(lst[j])<int(lst[i]) and int(lst[j])<int(lst[k])
                if a or b:
                   count+=1
                i+=1
                j+=1
                k+=1
            return count
        total=0
        for i in range(num1,num2+1):
            x=waviness(i)
            total+=x
        return total
                
               


        