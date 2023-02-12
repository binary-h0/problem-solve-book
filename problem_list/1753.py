# 그래프 이론, 다익스트라
import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra():
    global graph, k, v
    dist = [inf for _ in range(v + 1)]
    dist[k] = 0
    que = []
    heapq.heappush(que, (dist[k], k))

    while que:
        d, n = heapq.heappop(que)
        if dist[n] < d:
            continue
        for weight, node in graph[n]:
            sum_dist = weight + d
            if sum_dist < dist[node]:
                dist[node] = sum_dist
                heapq.heappush(que, (sum_dist, node))

    for i in range(1, v+1):
        if dist[i] == inf:
            print("INF")
        else:
            print(dist[i])

if __name__ == '__main__':
    v, e = map(int, input().rstrip().split())
    graph = [[] for _ in range(v+1)]
    k = int(input().rstrip())
    for _ in range(e):
        u, n, w = map(int, input().rstrip().split())
        graph[u].append( (w, n) )
    dijkstra()
