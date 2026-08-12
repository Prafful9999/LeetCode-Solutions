class MedianFinder:

    def __init__(self):
        self.heap1=[]
        self.heap2=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap1,-num)
        heapq.heappush(self.heap2,-heapq.heappop(self.heap1))
        if len(self.heap2)>len(self.heap1):
            heapq.heappush(self.heap1,-heapq.heappop(self.heap2))

    def findMedian(self) -> float:
       if len(self.heap1)>len(self.heap2):
        return -self.heap1[0]
       else:
        return (-self.heap1[0]+self.heap2[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()