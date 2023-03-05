import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
R, C = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(R)]
memo = [[-1] * C for _ in range(R)]
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def solve(r, c, visited):
    ans = 1
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not ((0 <= nr < R) and (0 <= nc < C)):
            continue
        idx = ord(graph[nr][nc]) - 65
        if visited[idx]:
            continue
        visited[idx] = True
        ans = max(solve(nr, nc, visited) + 1, ans)
        visited[idx] = False
    return ans

def main():
    visited = [False for _ in range(26)]
    visited[ord(graph[0][0]) - 65] = True
    print(solve(0, 0, visited))
main()

