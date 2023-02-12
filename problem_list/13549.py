# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 다익스트라, 0-1 너비 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline

visited = [0] * 200000

def bfs(start, end):
    que = deque()
    visited[start] = 1
    que.append((0, start))
    while que:
        t, n = que.popleft()
        if n == end:
            print(t)
            return
        next_pos = 2 * n
        if (0 <= next_pos < 200000):
            if not visited[next_pos]:
                visited[next_pos] = 1
                que.append((t, next_pos))

        next_pos = n - 1
        if (0 <= next_pos < 200000):
            if not visited[next_pos]:
                visited[next_pos] = 1
                que.append((t+1, next_pos))

        next_pos = n + 1
        if (0 <= next_pos < 200000):
            if not visited[next_pos]:
                visited[next_pos] = 1
                que.append((t+1, next_pos))

if __name__ == '__main__':
    N, K = map(int, input().split())
    bfs(N, K)
