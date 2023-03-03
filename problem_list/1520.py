# 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 깊이 우선 탐색
import sys
input = sys.stdin.readline
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
M, N = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(M)]
memo = [[-1] * N for _ in range(M)]
def solve(r, c):
    if (r == M - 1) and (c == N - 1):
        return 1
    if memo[r][c] != -1:
        return memo[r][c]

    count = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not ((0 <= nr < M) and (0 <= nc < N)):
            continue
        if graph[r][c] <= graph[nr][nc]:
            continue
        count += solve(nr, nc)
    memo[r][c] = count
    return memo[r][c]

if __name__ == '__main__':
    solve(0, 0)
    print(memo[0][0])