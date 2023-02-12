# 그래프 이론, 그래프 탐색, 플로이드-워셜
import sys
sys.setrecursionlimit(10**8)
input = __import__('sys').stdin.readline

s = set()

def find(n, x):
    for i in range(len(graph[x])):
        if graph[x][i] and visited[x][i] != n:
            visited[x][i] = n
            s.add(i)
            find(n, i)

def solve(n):
    global ans
    s.clear()
    for i in range(len(graph[n])):
        if graph[n][i]:
            s.add(i)
            find(n, i)
    while len(s) > 0:
        ans[n][s.pop()] = 1


if __name__ == '__main__':
    n = int(input().rstrip())
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
    visited = [[-1 for _ in range(n)] for __ in range(n)]
    ans = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        solve(i)
    for i in range(n):
        print(*ans[i])