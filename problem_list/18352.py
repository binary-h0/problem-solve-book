# 그래프 이론, 그래프 탐색, 너비우선탐색, 다익스트라
import sys
from collections import deque
input = sys.stdin.readline

def solve(graph, k, x, n):
    que = deque()
    visited = [False for _ in range(n + 1)]
    que.append((x, 0))
    visited[x] = True
    answer = []
    while que:
        city, w = que.popleft()
        if w == k:
            answer.append(city)
            continue
        for next_city in graph[city]:
            if visited[next_city]:
                continue
            visited[next_city] = True
            que.append((next_city, w + 1))
    answer.sort()
    if len(answer) == 0:
        print(-1)
    else:
        for i in answer:
            print(i)

if __name__ == '__main__':
    N, M, K, X = map(int, input().rstrip().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().rstrip().split())
        graph[s].append(e)

    solve(graph, K, X, N)