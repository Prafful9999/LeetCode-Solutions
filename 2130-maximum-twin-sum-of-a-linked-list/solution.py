# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dic={}
        ind=0
        n=0
        curr=head
        while curr!=None:
            n+=1
            curr=curr.next
        maxi=float('-inf')
        while head!=None:
            if (n-1)-ind in dic:
                maxi=max(maxi,head.val+dic[n-1-ind])
            else:
               dic[ind]=head.val
            ind+=1
            head=head.next
        return maxi

        

        