# 구현, 브루트포스, 백트래킹
import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
N, M, H = map(int, input().rstrip().split())
ans = []

def simulate(graph):
    for c in range(N):
        tmp = c
        for r in range(H):
            tmp += graph[r][tmp]
        if not tmp == c:
            return False
    return True

def solve(graph, count, i, j):
    while i < H:
        j = 0
        while j < N-1:
            if (graph[i][j] == 0) and (graph[i][j+1] == 0):
                graph[i][j] = 1
                graph[i][j + 1] = -1
                if simulate(graph):
                    graph[i][j] = 0
                    graph[i][j + 1] = 0
                    ans.append(count)
                    return
                if count < 3:
                    solve(graph, count+1, i, j)
                graph[i][j] = 0
                graph[i][j + 1] = 0
            j += 1
        i += 1

if __name__ == '__main__':
    info = [tuple(map(int, input().rstrip().split())) for _ in range(M)]
    graph = [[0 for __ in range(N)] for _ in range(H)]
    for r, c in info:
        graph[r-1][c-1], graph[r-1][c] = 1, -1
    if simulate(graph):
        print(0)
    else:
        solve(graph, 1, 0, 0)
        if len(ans) == 0:
            print(-1)
        else:
            print(min(ans))