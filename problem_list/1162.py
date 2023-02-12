# 다이나믹 프로그래밍, 그래프 이론, 다익스트라
import sys
import heapq
input = sys.stdin.readline

def Dijkstra(graph, n, k):
    dist = [[1000000000000 for __ in range(k + 1)] for _ in range(n + 1)]
    for i in range(k+1):
        dist[1][i] = 0
    heap = []
    heapq.heappush(heap, (0, 1, 0))
    while heap:
        s, node, c = heapq.heappop(heap)
        if dist[node][c] < s:
            continue
        if c < k:
            for next_node, next_s in graph[node]:
                if dist[next_node][c+1] > s:
                    dist[next_node][c+1] = s
                    heapq.heappush(heap, (s, next_node, c + 1))
        for next_node, next_s in graph[node]:
            sum_s = s + next_s
            if dist[next_node][c] > sum_s:
                dist[next_node][c] = sum_s
                heapq.heappush(heap, (sum_s, next_node, c))

    print(min(dist[n]))

if __name__ == '__main__':
    N, M, K = map(int, input().rstrip().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, s = map(int, input().rstrip().split())
        graph[a].append((b, s))
        graph[b].append((a, s))
    Dijkstra(graph, N, K)