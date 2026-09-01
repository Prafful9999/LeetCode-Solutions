# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp=head
        count=0
        arr=[]
        while temp.next.next!=None:
            count+=1
            if temp.next.val>temp.val and temp.next.val>temp.next.next.val:
                arr.append(count+1)
            elif temp.next.val<temp.val and temp.next.val<temp.next.next.val:
                arr.append(count+1)
            temp=temp.next

        if len(arr)==2:
            return [arr[-1]-arr[0]]*2
        if len(arr)<=1:
            return [-1,-1]
        mini=float('inf')
        for i in range(1,len(arr)):
            mini=min(mini,arr[i]-arr[i-1])
        maxi=arr[-1]-arr[0]
        return [mini,maxi]


            


        