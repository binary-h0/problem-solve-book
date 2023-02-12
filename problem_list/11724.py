# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    u = que.popleft()
    for i in graph[u]:
        if not visited[i]:
            que.append(i)
            visited[u] = True

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    graph = [[] for __ in range(n)]
    visited = [False for _ in range(n)]
    que = deque()
    ans = 0
    for _ in range(m):
        u, v = map(int, input().rstrip().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    for _ in range(n):
        u = _
        if not visited[u]:
            ans += 1
            que.append(u)
            visited[u] = True
            while len(que):
                bfs()
    print(ans)
