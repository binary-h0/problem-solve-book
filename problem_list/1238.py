# 그래프 이론, 다익스트라
import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def Dijkstra(s, graph, dist):
    heap = []
    dist[s] = 0
    heapq.heappush(heap, (0, s))
    while heap:
        weight, node = heapq.heappop(heap)
        if dist[node] < weight:
            continue
        for next_w, next_n in graph[node]:
            sum_w = next_w + weight
            if sum_w < dist[next_n]:
                dist[next_n] = sum_w
                heapq.heappush(heap, (sum_w, next_n))


if __name__ == '__main__':
    N, M, X = map(int, input().rstrip().split())
    graph = [[]for _ in range(N + 1)]
    reverseGraph = [[] for _ in range(N + 1)]
    dis1 = [inf for _ in range(N + 1)]
    dis2 = [inf for _ in range(N + 1)]
    for _ in range(M):
        s, e, w = map(int, input().rstrip().split())
        graph[s].append((w, e))
        reverseGraph[e].append((w, s))
    Dijkstra(X, graph, dis1)
    Dijkstra(X, reverseGraph, dis2)
    print(max(list(dis1[i] + dis2[i] for i in range(1, N+1))))