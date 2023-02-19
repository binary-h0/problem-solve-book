# 그래프 이론, 다익스트라, 플로이드-워셜
import sys
import heapq
input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())
item_lis = list(map(int, input().rstrip().split()))
graph = [[] for _ in range(n+1)]

def Dijkstra(node):
    dist = [99999999 for _ in range(n+1)]
    heap = []
    heapq.heappush(heap, (0, node))
    dist[node] = 0
    item_count = 0
    while heap:
        weight, node = heapq.heappop(heap)
        if weight > dist[node]:
            continue
        for next_node, next_weight in graph[node]:
            sum_weight = next_weight + weight
            if (dist[next_node] > sum_weight) and (m >= sum_weight):
                dist[next_node] = sum_weight
                heapq.heappush(heap, (sum_weight, next_node))
    for i in range(n):
        if dist[i+1] <= m:
            item_count += item_lis[i]
    return item_count

def solve():
    ans = 0
    for i in range(n):
        ret = Dijkstra(i+1)
        if ret > ans:
            ans = ret
    print(ans)

if __name__ == '__main__':
    for _ in range(r):
        a, b, l = map(int, input().rstrip().split())
        graph[a].append((b, l))
        graph[b].append((a, l))
    solve()