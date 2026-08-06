from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        undirected = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)
            undirected[u].append(v)
            undirected[v].append(u)

        suspicious = [False] * n

        def dfs(node):
            suspicious[node] = True
            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

        visited = [False] * n

        def dfs2(node):
            visited[node] = True
            for nei in undirected[node]:
                if not visited[nei]:
                    suspicious[nei] = False
                    dfs2(nei)

        for i in range(n):
            if not suspicious[i] and not visited[i]:
                dfs2(i)

        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans
        