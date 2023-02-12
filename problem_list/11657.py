# 그래프 이론, 벨만-포드
import sys
input = sys.stdin.readline
inf = sys.maxsize

edges = []

def BellmanFord(start, dist):
    dist[start] = 0
    for _ in range(N-1):
        for edge in edges:
            v_from, v_to, cost = edge
            if dist[v_from] == inf:
                continue
            if dist[v_to] > dist[v_from] + cost:
                dist[v_to] = dist[v_from] + cost
    for edge in edges:
        v_from, v_to, cost = edge
        if dist[v_from] == inf:
            continue
        if dist[v_to] > dist[v_from] + cost:
            return False
    return True

if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    dist = [inf] * (N + 1)
    for _ in range(M):
        edges.append(tuple(map(int, input().rstrip().split())))

    if BellmanFord(1, dist):
        for i in range(2, N+1):
            if dist[i] == inf:
                print(-1)
            else:
                print(dist[i])
    else:
        print(-1)