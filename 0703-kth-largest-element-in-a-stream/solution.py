class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

        # Min heap banao
        for i in range(len(self.nums) // 2 - 1, -1, -1):
            self.heapify_down(i)

        # Sirf k largest elements rakho
        while len(self.nums) > k:
            self.nums[0] = self.nums.pop()
            self.heapify_down(0)

    def heapify_up(self, ind):
        if ind == 0:
            return

        parent = (ind - 1) // 2

        if self.nums[parent] > self.nums[ind]:
            self.nums[parent], self.nums[ind] = \
                self.nums[ind], self.nums[parent]

            self.heapify_up(parent)

    def heapify_down(self, ind):
        smallest = ind

        left = 2 * ind + 1
        right = 2 * ind + 2

        if left < len(self.nums) and self.nums[left] < self.nums[smallest]:
            smallest = left

        if right < len(self.nums) and self.nums[right] < self.nums[smallest]:
            smallest = right

        if smallest != ind:
            self.nums[ind], self.nums[smallest] = \
                self.nums[smallest], self.nums[ind]

            self.heapify_down(smallest)

    def add(self, val: int) -> int:

        # New element insert
        self.nums.append(val)
        self.heapify_up(len(self.nums) - 1)

        # k se zyada hua -> smallest remove
        if len(self.nums) > self.k:
            self.nums[0] = self.nums.pop()
            self.heapify_down(0)

        # Root = kth largest
        return self.nums[0]