class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        freq = Counter(nums)
        heap = []

        for i in freq.keys():
            heap.append(i)

        def heapify(ind):
            largest = ind
            left = 2 * ind + 1
            right = 2 * ind + 2

            if left < len(heap) and freq[heap[left]] > freq[heap[largest]]:
                largest = left

            if right < len(heap) and freq[heap[right]] > freq[heap[largest]]:
                largest = right

            if largest != ind:
                heap[largest], heap[ind] = heap[ind], heap[largest]
                heapify(largest)

        # Build max heap
        for i in range(len(heap)//2 - 1, -1, -1):
            heapify(i)

        ans = []

        for i in range(k):
            ans.append(heap[0])

            if len(heap) == 1:
                heap.pop()
                break

            heap[0] = heap.pop()
            heapify(0)

        return ans