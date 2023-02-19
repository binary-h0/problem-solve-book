import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def solve(viruses, void_num):
    visited = [[False for _ in range(N)] for __ in range(N)]
    que = deque()
    for r, c in viruses:
        que.append((r, c, 0))
        visited[r][c] = True
    while que:
        r, c, t = que.popleft()
        if graph[r][c] == 0:
            void_num -= 1
        if void_num == 0:
            return t
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not ((0 <= nr < N) and (0 <= nc < N)):
                continue
            if visited[nr][nc]:
                continue
            if (graph[nr][nc] == 0) or (graph[nr][nc] == 2):
                que.append((nr, nc, t+1))
                visited[nr][nc] = True
            else:
                visited[nr][nc] = True
    if void_num == 0:
        return t
    else:
        return -1

if __name__ == '__main__':
    viruses_coord = []
    void_num = 0
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 2:
                viruses_coord.append((r, c))
            elif graph[r][c] == 0:
                void_num += 1
    ans = 99999
    for viruses in combinations(viruses_coord, M):
        ret = solve(viruses, void_num)
        if ret == -1:
            continue
        else:
            if ans > ret:
                ans = ret
    if ans == 99999:
        print(-1)
    else:
        print(ans)