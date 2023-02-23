# 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input().rstrip())
graph = [[] for _ in range(N+1)]
r_n, d = 0, 0

def dfs(visited, n, w):
    global r_n, d
    visited[n] = True
    if w > d:
        d, r_n = w, n
    for next_n, dist in graph[n]:
        sum_dist = dist + w
        if not visited[next_n]:
            dfs(visited, next_n, sum_dist)

def solve(node):
    global r_n, d
    visited = [False for _ in range(N+1)]
    dfs(visited, node, 0)
    visited, d = [False for _ in range(N + 1)], 0
    dfs(visited, r_n, 0)
    print(d)

if __name__ == '__main__':
    for _ in range(N-1):
        r, s, w = map(int, input().rstrip().split())
        graph[r].append((s, w))
        graph[s].append((r, w))
    solve(1)