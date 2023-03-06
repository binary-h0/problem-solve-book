# 그래프 이론, 최소 스패닝 트리
import math
import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
parents = [i for i in range(N + 1)]
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
coords = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
edges = []
for comb in combinations(range(N), 2):
    a, b = comb
    d = math.sqrt((coords[a][0] - coords[b][0]) ** 2 + (coords[a][1] - coords[b][1]) ** 2)
    edges.append((d, a+1, b+1))
edges.sort()

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    union(u, v)

if __name__ == '__main__':
    total = 0
    for edge in edges:
        d, u, v = edge
        if find(u) != find(v):
            union(u, v)
            total += d
    print("%.2f" % (round(total, 2)))