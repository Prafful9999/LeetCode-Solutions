class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic={}
        for i in tasks:
            dic[i]=dic.get(i,0)+1
        max_freq=max(dic.values())
        max_count=0
        for i in dic.values():
            if i==max_freq:
                max_count+=1
        formula=(max_freq-1)*(n+1)+max_count
        return max(formula,len(tasks))