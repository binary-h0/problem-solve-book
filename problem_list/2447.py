import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def solve(graph, n, r, c):
    d = n // 3
    if d == 0:
        return
    for i in range(d):
        for j in range(d):
            graph[r + d + i][c + d + j] = 0
    for i in range(0, n, d):
        for j in range(0, n, d):
            solve(graph, d, r + i, c + j)

def printer(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j]:
                print('*', end='')
            else:
                print(' ', end='')
        print()

if __name__ == '__main__':
    n = int(input().rstrip())
    graph = [[1 for _ in range(n)] for __ in range(n)]
    solve(graph, n, 0, 0)
    printer(graph)