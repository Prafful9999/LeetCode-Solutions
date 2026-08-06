# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        while fast!=None:
            slow=slow.next
            fast=fast.next.next
        temp=slow
        front=slow.next
        prev=None
        while temp!=None:
            temp.next=prev
            prev=temp
            temp=front
            if front!=None:
              front=front.next
        maxi=float('-inf')
        while prev!=None and head!=slow:
            maxi=max(maxi,prev.val+head.val)
            head=head.next
            prev=prev.next
        return maxi

