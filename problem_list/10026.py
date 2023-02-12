# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(col):
    global que, n, img, visited

    while len(que) > 0:
        x, y = que.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if not ((0 <= nx < n) and (0 <= ny < n)):
                continue
            if (img[nx][ny] != col) or visited[nx][ny] == 1:
                continue
            visited[nx][ny] = 1
            que.append((nx, ny))

if __name__ == '__main__':
    que = deque()
    n = int(input().rstrip())
    img = [list(input().rstrip()) for _ in range(n)]
    a = [[0 for _ in range(n)] for __ in range(n)]
    b = [[0 for _ in range(n)] for __ in range(n)]
    visited = [[0 for _ in range(n)] for __ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if (visited[i][j] == 1):
                continue
            que.append((i, j))
            visited[i][j] = 1
            count += 1
            bfs(img[i][j])
    print(count, end=' ')
    visited = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if img[i][j] == 'G':
                img[i][j] = 'R'
    count = 0
    for i in range(n):
        for j in range(n):
            if (visited[i][j] == 1):
                continue
            que.append((i, j))
            visited[i][j] = 1
            count += 1
            bfs(img[i][j])
    print(count)