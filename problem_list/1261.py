import sys
from collections import deque
input = sys.stdin.readline

def solve(graph, n, m):
    visited = [[False for _ in range(n)] for __ in range(m)]
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    que = deque()
    que.append((0, 0))
    visited[0][0] = True
    count = 0
    que1 = deque()
    while True:
        while que:
            r, c = que.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if (0 <= nr < m) and (0 <= nc < n):
                    if visited[nr][nc]:
                        continue
                    if graph[nr][nc] == 0:
                        visited[nr][nc] = True
                        que.append((nr, nc))
                    elif graph[nr][nc] == 1:
                        visited[nr][nc] = True
                        que1.append((nr, nc))
        if visited[m - 1][n - 1]:
            break
        count += 1
        while que1:
            que.append(que1.pop())
    print(count)

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    graph = [[0 for _ in range(n)] for __ in range(m)]
    for i in range(m):
        s = input().rstrip()
        for j in range(n):
            graph[i][j] = int(s[j])

    solve(graph, n, m)