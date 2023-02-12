import sys
import heapq
input = sys.stdin.readline

def Dijkstra(graph, s):
    dist = [2000000000 for _ in range(len(graph))]
    dist[s] = 0
    heap = []
    heapq.heappush(heap, (0, s))
    while heap:
        d, node = heapq.heappop(heap)
        if dist[node] < d:
            continue
        for next_node, next_dist in graph[node]:
            sum_dist = d + next_dist
            if sum_dist < dist[next_node]:
                dist[next_node] = sum_dist
                heapq.heappush(heap, (sum_dist, next_node))
    return dist

def solve():
    n, m, t = map(int, input().rstrip().split())
    s, g, h = map(int, input().rstrip().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().rstrip().split())
        graph[a].append((b, d * 2))
        graph[b].append((a, d * 2))
    for i in range(len(graph[g])):
        if graph[g][i][0] == h:
            graph[g][i] = (h, graph[g][i][1] - 1)
    for i in range(len(graph[h])):
        if graph[h][i][0] == g:
            graph[h][i] = (g, graph[h][i][1] - 1)

    candidate_lis = [int(input().rstrip()) for _ in range(t)]
    candidate_lis.sort()
    dist = Dijkstra(graph, s)
    answer = []
    for node in candidate_lis:
        if dist[node] % 2 == 1:
            answer.append(node)
    print(*answer)

if __name__ == '__main__':
    for _ in range(int(input().rstrip())):
        solve()