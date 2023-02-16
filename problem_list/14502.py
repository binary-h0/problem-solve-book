import sys
from collections import deque
input = sys.stdin.readline
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
viruses = []
voids = []

def simulate(graph):
    visited = [[False for _ in range(8)] for __ in range(8)]
    increased_viruse_num = 0
    que = deque()
    for r, c in viruses:
        que.append((r, c))
    while que:
        r, c = que.popleft()
        increased_viruse_num += 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not ((0 <= nr < len(graph)) and (0 <= nc < len(graph[0]))):
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = True
            if graph[nr][nc] == 0:
                que.append((nr, nc))
    return increased_viruse_num


def solve(graph):
    ans = []
    for i1 in range(0, len(voids) - 2):
        w1_r, w1_c = voids[i1]
        for i2 in range(i1 + 1, len(voids) - 1):
            w2_r, w2_c = voids[i2]
            for i3 in range(i2, len(voids)):
                w3_r, w3_c = voids[i3]
                graph[w1_r][w1_c], graph[w2_r][w2_c], graph[w3_r][w3_c] = 1, 1, 1
                ans.append(simulate(graph))
                graph[w1_r][w1_c], graph[w2_r][w2_c], graph[w3_r][w3_c] = 0, 0, 0
    return min(ans)

if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
    void_num = -3
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 2:
                viruses.append((r, c))
            elif graph[r][c] == 0:
                voids.append((r, c))
                void_num += 1
    void_num -= solve(graph) - len(viruses)
    print(void_num)