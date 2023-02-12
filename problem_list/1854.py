import sys
import heapq
input = sys.stdin.readline

def Dijkstra(graph, n, k):
    dist = [[10000000000 for __ in range(k + 1)] for _ in range(n + 1)]
    dist[1][0] = 0
    heap = []
    heapq.heappush(heap, (0, 1))
    while heap:
        weight, node = heapq.heappop(heap)
        for next_node, next_weight in graph[node]:
            sum_weight = weight + next_weight
            if sum_weight < dist[next_node][k]:
                dist[next_node][k] = sum_weight
                dist[next_node].sort()
                heapq.heappush(heap, (sum_weight, next_node))
    for i in range(1, n + 1):
        if dist[i][k-1] == 10000000000:
            print(-1)
        else:
            print(dist[i][k-1])

if __name__ == '__main__':
    n, m, k = map(int, input().rstrip().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, w, = map(int, input().rstrip().split())
        graph[s].append((e, w))
    Dijkstra(graph, n, k)