# 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(i, j, level, time, visit):
    global stage, visited
    que = deque()
    que.append((i, j, time))
    lis = []
    while len(que) > 0:
        x, y, t = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not ((0 <= nx < n) and (0 <= ny < n)):
                continue
            if (stage[nx][ny] > level):
                continue
            if (visited[nx][ny] == visit):
                continue
            if (0 < stage[nx][ny] < level):
                lis.append((nx, ny, t + 1))
                visited[nx][ny] = visit
            que.append((nx, ny, t + 1))
            visited[nx][ny] = visit
    lis.sort(key=lambda x: (x[2], x[0], x[1]))
    return lis

def solve(i, j):
    global stage, visited
    level = 2
    exp = 0
    time = 0
    visit = -1
    visited[i][j] = visit
    lis = [(i, j, time)]
    while len(lis) > 0:
        x, y, t = lis[0][0], lis[0][1], lis[0][2]
        stage[x][y] = 0
        lis = bfs(x, y, level, t, visit)
        exp += 1
        visit -= 1
        time = t
        if exp == level:
            level += 1
            exp = 0

    print(time)

if __name__ == '__main__':
    n = int(input().rstrip())
    stage = [list(map(int, input().rstrip().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for __ in range(n)]
    sx, sy = 0, 0
    for i in range(n):
        for j in range(n):
            if stage[i][j] == 9:
                sx, sy = i, j
                stage[i][j] = 0
                break
    solve(sx, sy)
