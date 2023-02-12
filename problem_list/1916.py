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
    N = int(input().rstrip())
    M = int(input().rstrip())
    graph = [[] for _ in range(N+1)]
    dist = [inf for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().rstrip().split())
        graph[s].append((e, w))
    A, B = map(int, input().rstrip().split())
    Dijkstra(A, dist)
    print(dist[B])