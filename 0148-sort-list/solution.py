# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Function to split the linked list into two halves
        def getMid(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return mid

        # Function to merge two sorted linked lists
        def merge(left, right):
            dummy = ListNode()
            tail = dummy

            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next

            tail.next = left if left else right
            return dummy.next

        mid = getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)

        return merge(left, right)
