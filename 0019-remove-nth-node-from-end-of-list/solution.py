# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        elif head.next.next==None:
            if n==1:
                head.next=None
                return head
            else:
                return head.next
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        if length==n:
            return head.next
        curr=head
        for i in range((length-n)-1):
            curr=curr.next
        if curr.next and curr.next.next:
            curr.next=curr.next.next
        elif curr.next.next==None:
            curr.next=None  
        return head


        

        