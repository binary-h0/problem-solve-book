# 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색
import sys
input = sys.stdin.readline

def solve(graph, n):
    memory = [[[0 for _ in range(n)] for __ in range(n)] for ___ in range(3)]
    memory[0][0][1] = 1
    for i in range(2, n):
        if graph[0][i] == 0:
            memory[0][0][i] = memory[0][0][i - 1]
    for r in range(1, n):
        for c in range(1, n):
            if graph[r][c] == 0 and graph[r][c - 1] == 0 and graph[r - 1][c] == 0:
                memory[2][r][c] = memory[0][r-1][c-1] + memory[1][r-1][c-1] + memory[2][r-1][c-1]
            if graph[r][c] == 0:
                memory[0][r][c] = memory[0][r][c-1] + memory[2][r][c-1]
                memory[1][r][c] = memory[1][r-1][c] + memory[2][r-1][c]
    print(memory[0][n-1][n-1] + memory[1][n-1][n-1] + memory[2][n-1][n-1])

def main():
    N = int(input().rstrip())
    graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
    solve(graph, N)
main()