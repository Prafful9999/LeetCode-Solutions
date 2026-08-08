class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        import heapq
        dic=Counter(hand)
        n=len(hand)
        if n%groupSize!=0:
            return False
        heap=[]
        for i in dic:
            heapq.heappush(heap,i)
        while len(heap)!=0:
            start=heap[0]
            for i in range(start,start+groupSize):
                if dic[i]==0:
                    return False
                else:
                    dic[i]-=1
            while len(heap)>0 and dic[heap[0]]==0:
                heapq.heappop(heap)
        return True