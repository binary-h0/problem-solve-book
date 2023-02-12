# 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global route
    que = deque()
    que.append((1, 0))
    while len(que) > 0:
        x, tryCount = que.popleft()
        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue
            if route[nx] == -1:
                continue
            if route[nx] == 0:
                route[nx] = -1
                que.append((nx, tryCount + 1))
            else:
                que.append((route[nx], tryCount + 1))
                route[route[nx]] = -1
                route[nx] = -1
        if x == 100:
            print(tryCount)
            break

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    route = [0 for _ in range(101)]
    for _ in range(n):
        x, y = map(int, input().rstrip().split())
        route[x] = y
    for _ in range(m):
        x, y = map(int, input().rstrip().split())
        route[x] = y
    bfs()
