# 그래프 이론, 다익스트라
import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def Dijkstra(start, dist):
    global graph
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        weight, node = heapq.heappop(heap)
        if dist[node] < weight:
            continue
        for next_node, next_weight in graph[node]:
            sum_weight = weight + next_weight
            if sum_weight < dist[next_node]:
                dist[next_node] = sum_weight
                heapq.heappush(heap, (sum_weight, next_node))

if __name__ == '__main__':
    N, E = map(int, input().rstrip().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().rstrip().split())
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))
    V1, V2 = map(int, input().rstrip().split())
    V1toV2Dist = [inf for _ in range(N + 1)]
    start1Dist = [inf for _ in range(N+1)]
    startNDist = [inf for _ in range(N+1)]
    Dijkstra(1, start1Dist)
    Dijkstra(N, startNDist)
    Dijkstra(V1, V1toV2Dist)
    pathDistance1 = 0
    pathDistance2 = 0
    pathDistance1 += V1toV2Dist[V2]
    pathDistance2 += V1toV2Dist[V2]
    pathDistance1 += start1Dist[V1]
    pathDistance1 += startNDist[V2]
    pathDistance2 += start1Dist[V2]
    pathDistance2 += startNDist[V1]
    ans = min(pathDistance1, pathDistance2)
    if ans >= inf:
        print(-1)
    else:
        print(ans)
