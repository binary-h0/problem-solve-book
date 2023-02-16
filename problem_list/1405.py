import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
lis = list(map(int, input().rstrip().split()))
N = lis[0]
visited = [[False for _ in range(N * 2 + 1)] for __ in range(N * 2 + 1)]
answer = 0

def dfs(r, c, n, p):
    global answer
    if n == N:
        answer += p
        return
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if visited[nr][nc]:
            continue
        visited[nr][nc] = True
        dfs(nr, nc, n + 1, p*lis[i+1])
        visited[nr][nc] = False

def solve():
    r, c = N-1, N-1
    visited[r][c] = True
    dfs(r, c, 0, 1)
    print(answer* (0.01 ** N))

if __name__ == '__main__':
    solve()