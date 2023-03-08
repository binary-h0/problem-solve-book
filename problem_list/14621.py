# 최소 스패닝 트리, 그래프 이론
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lis = list(input().rstrip().split())
edges = [tuple(map(int, input().rstrip().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])
parents = [i for i in range(N+1)]
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]
def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
total = 0
total_node = 1
for edge in edges:
    u, v, d = edge
    a, b = find(u), find(v)
    if (a != b) and (lis[u-1] != lis[v-1]):
        total += d
        union(u, v)
        total_node += 1
print(total) if total_node == N else print(-1)
