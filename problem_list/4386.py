# 그래프 이론, 최소 스패닝 트리, 조합
import math
import sys
from itertools import combinations
input = sys.stdin.readline

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    parents_x = find(parents, x)
    parents_y = find(parents, y)
    if parents_x < parents_y:
        parents[parents_y] = parents_x
    else:
        parents[parents_x] = parents_y

if __name__ == '__main__':
    n = int(input().rstrip())
    coords = [tuple(map(float, input().rstrip().split())) for _ in range(n)]
    parents = [i for i in range(n)]
    edges = []
    for comb in combinations(parents, 2):
        a, b = comb
        c = math.sqrt((coords[a][0] - coords[b][0]) ** 2 + (coords[a][1] - coords[b][1]) ** 2)
        edges.append((c, a, b))
    edges.sort()
    total_weight = 0
    for edge in edges:
        w, u, v = edge
        if find(parents, u) != find(parents, v):
            union(parents, u, v)
            total_weight += w
    print(total_weight)