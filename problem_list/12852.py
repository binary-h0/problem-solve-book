# 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색
from collections import deque

def bfs(graph, memo, target):
    que = deque()
    que.append(1)
    graph[1] = 1
    memo[1] = [1]
    while que:
        n = que.popleft()
        if n == target:
            print(len(memo[target]) -1)
            print(*memo[target][::-1])
        nx = n + 1
        if (nx <= target):
            if (graph[nx] == 0):
                tmp = memo[n][:]
                tmp.append(nx)
                memo[nx] = tmp
                graph[nx] = 1
                que.append(nx)
        nx = n * 2
        if (nx <= target):
            if (graph[nx] == 0):
                tmp = memo[n][:]
                tmp.append(nx)
                memo[nx] = tmp
                graph[nx] = 1
                que.append(nx)
        nx = n * 3
        if (nx <= target):
            if (graph[nx] == 0):
                tmp = memo[n][:]
                tmp.append(nx)
                memo[nx] = tmp
                graph[nx] = 1
                que.append(nx)

def main():
    n = int(input())
    graph = [0 for _ in range(n+1)]
    memo = [[] for _ in range(n+1)]
    bfs(graph, memo, n)

main()