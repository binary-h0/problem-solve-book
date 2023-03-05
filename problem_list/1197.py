import sys

# Union-find 구현을 위한 함수
def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    parent_x = find(parents, x)
    parent_y = find(parents, y)
    if parent_x < parent_y:
        parents[parent_y] = parent_x
    else:
        parents[parent_x] = parent_y

# 입력
V, E = map(int, sys.stdin.readline().split())
edges = []
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b)) # 가중치, 정점 a, 정점 b

# Kruskal's algorithm
parents = [i for i in range(V+1)]
edges.sort()
total_weight = 0
for edge in edges:
    weight, u, v = edge
    if find(parents, u) != find(parents, v):
        union(parents, u, v)
        total_weight += weight

print(total_weight)
