# 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def countUnRoaten(m, n, h):
    global box, unRoaten, que
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    unRoaten += 1
                elif box[i][j][k] == 1:
                    que.append((i, j, k))
def bfs():
    global que, m, n, h, box, unRoaten
    piv = 1
    while len(que) > 0:
        z, x, y = que.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if not ((0 <= nx < n) and (0 <= ny < m) and (0 <= nz < h)):
                continue
            if not (box[nz][nx][ny] == 0):
                continue
            box[nz][nx][ny] = 1 + box[z][x][y]
            que.append((nz, nx, ny))
            unRoaten -= 1
        piv = box[z][x][y] - 1
    return piv


if __name__ == '__main__':
    m, n, h = map(int, input().rstrip().split())
    box = [[list(map(int, input().rstrip().split())) for __ in range(n)] for _ in range(h)]
    unRoaten, day = 0, 0
    que = deque()

    countUnRoaten(m, n, h)
    if not unRoaten:
        print(0)
    else:
        day = bfs()
        if unRoaten:
            print(-1)
        else:
            print(day)
