from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: Multi-source BFS to compute distance from nearest thief
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist[i][j] = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and dist[nr][nc] == -1
                ):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Maximum possible safeness
        high = 0
        for row in dist:
            high = max(high, max(row))

        # Step 2: Check if a path exists with safeness >= val
        def can(val):
            if dist[0][0] < val or dist[n - 1][n - 1] < val:
                return False

            q = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            while q:
                r, c = q.popleft()

                if r == n - 1 and c == n - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < n
                        and 0 <= nc < n
                        and not visited[nr][nc]
                        and dist[nr][nc] >= val
                    ):
                        visited[nr][nc] = True
                        q.append((nr, nc))

            return False

        # Step 3: Binary Search
        low = 0
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
        