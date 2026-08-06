class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(llst,rlst):
            i=0
            j=0
            count=0
            while j<len(rlst) and i<len(llst):
                if llst[i]>2*rlst[j]:
                    count+=(len(llst)-i)
                    j+=1
                else:
                    i+=1
            return count



        def mergesort(lst):
            n=len(lst)
            if n<=1:
                return lst,0
            mid=n//2
            lst1=lst[:mid]
            lst2=lst[mid:]
            leftlst,lcount=mergesort(lst1)
            rightlst,rcount=mergesort(lst2)
            crosscount=merge(leftlst,rightlst)
            merged=sorted(leftlst+rightlst)

            return merged,lcount+rcount+crosscount

        _,ans=mergesort(nums)
        return ans
