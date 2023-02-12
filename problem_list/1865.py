# 그래프 이론, 벨만-포드
import sys
input = sys.stdin.readline
inf = 2000000000

def Bellman_Ford(n):
    global graph

    dist = [inf for _ in range(n + 1)]
    dist[1] = 0
    for i in range(n-1):
        for j in range(len(graph)):
            s, e, w = graph[j]
            if dist[e] > dist[s] + w:
                dist[e] = dist[s] + w
    for j in range(len(graph)):
        s, e, w = graph[j]
        if dist[e] > dist[s] + w:
            print("YES")
            return
    print("NO")
    return

if __name__ == '__main__':
    for _ in range(int(input().rstrip())):
        N, M, W = map(int, input().rstrip().split())
        graph = []
        for __ in range(M):
            S, E, T = map(int, input().rstrip().split())
            graph.append((S, E, T))
        for __ in range(W):
            S, E, T = map(int, input().rstrip().split())
            graph.append((S, E, -T))
        Bellman_Ford(N)

from sys import stdin
input = stdin.readline

def bf():
    for i in range(n):
        for j in range(len(edges)):
            cur, next, cost = edges[j]
            if dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n - 1:
                    return True
    return False


TC = int(input())

for _ in range(TC):
    n, m, w = map(int, input().split())
    edges = []
    dist = [1e9] * (n + 1)
    for i in range(m + w):
        s, e, t = map(int, input().split())
        if i >= m:
            t = -t
        else:
            edges.append((e, s, t))
        edges.append((s, e, t))
    if bf():
        print("YES")
    else:
        print("NO")