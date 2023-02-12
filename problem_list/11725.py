import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input().rstrip())
ans = [1 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

def solve(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            ans[next_v] = v
            solve(next_v)
    return

if __name__ == '__main__':
    for _ in range(n-1):
        v1, v2 = map(int, input().rstrip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    solve(1)
    for i in range(2, n+1):
        print(ans[i])