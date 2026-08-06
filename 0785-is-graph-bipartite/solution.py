class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def bfs(start):
            queue = deque([start])
            color[start] = 0

            while queue:
                node = queue.popleft()

                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        queue.append(nei)

                    elif color[nei] == color[node]:
                        return False

            return True

        for i in range(n):
            if color[i] == -1:
                if not bfs(i):
                    return False

        return True
        

        