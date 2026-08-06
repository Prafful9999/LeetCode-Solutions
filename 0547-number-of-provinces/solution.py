class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import deque
        vis=[0 for _ in range(len(isConnected))]
        def bfs(n):
             que=deque([n])
             while len(que)!=0:
                node=que.popleft()
                if vis[node]==1:
                    continue
                vis[node]=1
                for i in range(len(isConnected[node])):
                    if isConnected[node][i]==1 and vis[i]==0:
                        que.append(i)
        count=0
        for i in range(len(vis)):
            if vis[i]==0:
                bfs(i)
                count+=1
        return count
