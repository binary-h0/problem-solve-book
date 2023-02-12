# 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs():
    global notRoaten
    r, c = que.popleft()
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if (-1 < nr < m) and (-1 < nc < n):
            if (not visited[nr][nc]) and (box[nr][nc] == 0):
                que.append((nr, nc))
                visited[nr][nc] = True
                notRoaten -= 1

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    box = [list(map(int, input().rstrip().split())) for _ in range(m)]
    visited = [[False for _ in range(n)] for __ in range(m)]
    que = deque()
    notRoaten = 0
    day = 0
    for r in range(m):
        for c in range(n):
            if box[r][c] == 1:
                que.append((r, c))
                visited[r][c] = True
            elif box[r][c] == 0:
                notRoaten += 1

    while notRoaten > 0:
        day += 1
        if len(que) == 0:
            break
        for _ in range(len(que)):
            bfs()
    if notRoaten == 0:
        print(day)
    else:
        print(-1)