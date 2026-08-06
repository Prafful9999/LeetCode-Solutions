class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

            while True:
                pro=1
                num=n
                while num>=10:
                    k=num%10
                    pro=pro*k
                    num=num//10
                pro=pro*num
                if pro%t==0:
                    return n
                n+=1
        

            