class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adj=[[] for _ in range(n+1)]
        for i in range(n):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1:
                    adj[i+1].append(j+1)
        vis=[0 for _ in range(len(adj))]
        def bfs(node):
            from collections import deque
            que=deque([node])
            while len(que)!=0:
                node=que.popleft()
                if vis[node]==1:
                    continue
                vis[node]=1
                for i in adj[node]:
                    if vis[i]==0:
                        que.append(i)
        count=0
        for i in range(1,len(vis)):
            if vis[i]==0:
                bfs(i)
                count+=1
        return count
        