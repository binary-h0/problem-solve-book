# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 다익스트라
import sys
import heapq
input = sys.stdin.readline

def solve(graph, n):
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    graph[0][0] = -1
    while heap:
        cost, r, c = heapq.heappop(heap)
        if (r == n-1) and (c == n-1):
            print(cost)
            return
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not ((0 <= nr < n) and (0 <= nc < n)):
                continue
            if graph[nr][nc] == -1:
                continue
            if graph[nr][nc] == 1:
                heapq.heappush(heap, (cost, nr, nc))
            elif graph[nr][nc] == 0:
                heapq.heappush(heap, (cost + 1, nr, nc))
            graph[nr][nc] = -1


if __name__ == '__main__':
    n = int(input().rstrip())
    graph = [list(map(int, input().rstrip())) for _ in range(n)]
    solve(graph, n)