# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline

def solve(graph, visited, r, c):
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    que = deque()
    que.append((r, c))
    if visited[r][c]:
        return 0
    visited[r][c] = True
    count = 0
    while que:
        r, c = que.popleft()
        count += 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not ((0 <= nr < len(graph)) and (0 <= nc < len(graph[0]))):
                continue
            if visited[nr][nc]:
                continue
            if graph[nr][nc] == 1:
                que.append((nr, nc))
                visited[nr][nc] = True
            else:
                visited[nr][nc] = True
    return count

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for __ in range(n)]
    count = 0
    max_size = 0
    for r in range(n):
        for c in range(m):
            if graph[r][c] == 1:
                ret = solve(graph, visited, r, c)
                if ret == 0:
                    continue
                count += 1
                if max_size < ret:
                    max_size = ret
    print(count)
    print(max_size)