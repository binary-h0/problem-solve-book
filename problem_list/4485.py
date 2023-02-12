# 그래프 이론, 다익스트라
import sys
import heapq
inf = sys.maxsize
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def Dijkstra(startX, startY, dist):
    global graph, n
    heap = []
    dist[startX][startY] = graph[startX][startY]
    heapq.heappush(heap, (graph[startX][startY], startX, startY))
    while heap:
        weight, x, y = heapq.heappop(heap)
        if dist[x][y] < weight:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not ((0 <= nx < n) and (0 <= ny < n)):
                continue
            sum_weight = graph[nx][ny] + weight
            if sum_weight < dist[nx][ny]:
                dist[nx][ny] = sum_weight
                heapq.heappush(heap, (sum_weight, nx, ny))

if __name__ == '__main__':
    i = 0
    while True:
        i += 1
        n = int(input().rstrip())
        if not n:
            break
        graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
        dist = [[inf for __ in range(n)] for _ in range(n)]
        Dijkstra(0, 0, dist)
        print("Problem {}: {}".format(i, dist[n-1][n-1]))