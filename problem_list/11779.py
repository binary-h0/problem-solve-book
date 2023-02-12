# 그래프 이론, 다익스트라
import sys
import heapq
input = sys.stdin.readline

def Dijksrtra(graph, s):
    dist = [[10000000000, 0] for _ in range(len(graph))]
    dist[s][0], dist[s][1] = 0, s
    heap = []
    heapq.heappush(heap, (0, s))
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node][0]:
            continue
        for next_node, next_cost in graph[node]:
            sum_cost = next_cost + cost
            if dist[next_node][0] > sum_cost:
                dist[next_node][0], dist[next_node][1] = sum_cost, node
                heapq.heappush(heap, (sum_cost, next_node))
    return dist

if __name__ == '__main__':
    n = int(input().rstrip())
    m = int(input().rstrip())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, w = map(int, input().rstrip().split())
        graph[s].append((e, w))
    s, e = map(int, input().rstrip().split())
    dist = Dijksrtra(graph, s)
    route = [e]
    count, before_node = 2, dist[e][1]
    while not (before_node == s):
        route.append(before_node)
        before_node = dist[before_node][1]
        count += 1
    route.append(before_node)
    print(dist[e][0])
    print(count)
    print(*route[::-1])