from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # Push always in q1
    def push(self, x: int) -> None:
        self.q1.append(x)

    # Pop: move n-1 elements to q2
    def pop(self) -> int:
        # Move all elements except last
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        # Last element = stack top
        popped = self.q1.popleft()

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return popped

    def top(self) -> int:
        # Same logic as pop but without deleting
        
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0
