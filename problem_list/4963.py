# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline

def solve(graph, w, h):
    dr, dc = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    visited = [[False] * w for _ in range(h)]
    que = deque()
    island = 0
    for r in range(h):
        for c in range(w):
            if visited[r][c]:
                continue
            if graph[r][c] == 0:
                visited[r][c] = True
            else:
                island += 1
                que.append((r, c))
                visited[r][c] = True
                while que:
                    _r, _c = que.popleft()
                    for i in range(8):
                        nr, nc = _r + dr[i], _c + dc[i]
                        if not ((0 <= nr < h) and (0 <= nc < w)):
                            continue
                        if visited[nr][nc]:
                            continue
                        visited[nr][nc] = True
                        if graph[nr][nc] == 1:
                            que.append((nr, nc))
    print(island)

if __name__ == '__main__':
    while 1:
        w, h = map(int, input().rstrip().split())
        if (w == 0) and (h == 0):
            break
        graph = [list(map(int, input().rstrip().split())) for _ in range(h)]
        solve(graph, w, h)