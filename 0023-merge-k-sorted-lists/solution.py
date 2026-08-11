class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        heap = []
        count = 0

        # Har linked list ka first node heap mein
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, count, head))
                count += 1

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, _, node = heapq.heappop(heap)

            # Node ko answer mein add karo
            curr.next = node
            curr = curr.next

            # Us node ka next node heap mein daalo
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1

        return dummy.next