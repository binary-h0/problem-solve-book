import sys
from collections import deque
# input = sys.stdin.readline

def solve(graph, visited, r, c):
    N, M = len(graph), len(graph[0])
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    que = deque()
    que.append((r, c))
    visited.add((r, c))
    while que:
        r, c = que.popleft()
        count = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not ((0 <= nr < N) and (0 <= nc < M)):
                continue
            if (nr, nc) in visited:
                continue
            if graph[nr][nc] <= 0:
                count += 1
            else:
                visited.add((nr, nc))
                que.append((nr, nc))
        graph[r][c] -= count

def main():
    N, M = map(int, input().rstrip().split())
    graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
    time = 0
    coords = set()
    for r in range(N):
        for c in range(M):
            coords.add((r, c))
    flag = True
    while coords:
        visited = set()
        count = 0
        save = set()
        for r, c in coords:
            if ((graph[r][c] > 0) and (not (r, c) in visited)):
                solve(graph, visited, r, c)
                count += 1
            if graph[r][c] < 1:
                save.add((r, c))
        if count > 1:
            print(time)
            flag = False
            break
        time += 1
        coords = coords - save
    if flag:
        print(0)
main()