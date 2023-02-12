# 다이나믹 프로그래밍, 누적 합
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
    for j in range(N):
        for i in range(1, N):
            graph[j][i] += graph[j][i - 1]
    for j in range(N):
        for i in range(1, N):
            graph[i][j] += graph[i - 1][j]

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().rstrip().split())
        if (x1 == 1) and (y1 == 1):
            print(graph[x2 - 1][y2 - 1])
        elif (x1 == 1) and (y1 != 1):
            print(graph[x2 - 1][y2 - 1] - graph[x2 - 1][y1 - 2])
        elif (x1 != 1) and (y1 == 1):
            print(graph[x2 - 1][y2 - 1] - graph[x1 - 2][y2 - 1])
        else:
            print(graph[x2 - 1][y2 - 1] - graph[x1 - 2][y2 - 1] - graph[x2 - 1][y1 - 2] + graph[x1 - 2][y1 - 2])