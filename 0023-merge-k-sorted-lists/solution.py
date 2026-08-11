class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        heap = []

        # Saare values heap mein daalo
        for head in lists:
            curr = head

            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next

        # Dummy linked list
        dummy = ListNode(0)
        curr = dummy

        # Heap se values nikaal kar linked list banao
        while heap:
            val = heapq.heappop(heap)

            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next