# 다이나믹 프로그래밍, 그래프 이론, 다익스트라
import sys
import heapq
input = sys.stdin.readline

def main():
    inf = 100000000
    for _ in range(int(input().rstrip())):
        N, M, K = map(int, input().rstrip().split())
        memory = [[inf for _ in range(N + 1)] for __ in range(M + 1)]
        graph = [[] for _ in range(N + 1)]
        for __ in range(K):
            u, v, c, d = map(int, input().rstrip().split())
            graph[u].append((v, c, d))
        heap = [(0, 0, 1)]
        while heap:
            dist, cost, node = heapq.heappop(heap)
            if dist > memory[cost][node]:
                continue
            for n_node, n_cost, n_dist in graph[node]:
                s_dist = n_dist + dist
                s_cost = n_cost + cost
                if (s_cost <= M) and (s_dist < memory[s_cost][n_node]):
                    heapq.heappush(heap, (s_dist, s_cost, n_node))
                    for i in range(s_cost, M + 1):
                        if memory[i][n_node] > s_cost:
                            memory[i][n_node] = s_cost
                        else:
                            break
        if memory[M][N] != inf:
            print(memory[M][N])
        else:
            print("Poor KCM")
main()