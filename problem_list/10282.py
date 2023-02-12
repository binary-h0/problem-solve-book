# 그래프 이론, 다익스트라
import sys
import heapq
input = sys.stdin.readline

def Dijkstra(graph, c):
    dist = [100000000 for _ in range(len(graph))]
    dist[c] = 0
    heap = []
    heapq.heappush(heap, (0, c))
    while heap:
        sec, com = heapq.heappop(heap)
        if dist[com] < sec:
            continue
        for next_com, next_sec in graph[com]:
            sum_sec = next_sec + sec
            if sum_sec < dist[next_com]:
                dist[next_com] = sum_sec
                heapq.heappush(heap, (sum_sec, next_com))
    return dist



def solve():
    n, d, c = map(int, input().rstrip().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().rstrip().split())
        graph[b].append((a, s))
    dist = Dijkstra(graph, c)
    count = 0
    max_sec = 0
    for i in range(len(dist)):
        if dist[i] == 100000000:
            continue
        count += 1
        if dist[i] > max_sec:
            max_sec = dist[i]
    print(count, max_sec)

if __name__ == '__main__':
    for _ in range(int(input().rstrip())):
        solve()