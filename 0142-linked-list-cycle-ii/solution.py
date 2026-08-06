# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        elif head.next.next==None:
            if head.next.next==head:
                return heaad
            else:
                return None
        else:
            slow=fast=head
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    ptr1=head
                    ptr2=slow
                    while ptr1!=ptr2:
                        ptr1=ptr1.next
                        ptr2=ptr2.next
                    return ptr1
            return None
