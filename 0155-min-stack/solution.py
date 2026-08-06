class MinStack:

    def __init__(self):
        self.mylist=[]
        

    def push(self, val: int) -> None:
        if len(self.mylist)==0:
            self.mylist.append([val,val])
        else:
            mini=min(self.mylist[-1][1],val)
            self.mylist.append([val,mini])
    
        

    def pop(self) -> None:
        return self.mylist.pop()
        

    def top(self) -> int:
        return self.mylist[-1][0]
        

    def getMin(self) -> int:
        return self.mylist[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()