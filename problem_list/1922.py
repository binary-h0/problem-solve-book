# 그래프 이론, 최소 스패닝 트리
import sys
input = sys.stdin.readline

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

if __name__ == '__main__':
    N = int(input().rstrip())
    M = int(input().rstrip())
    edges = [tuple(map(int, input().rstrip().split())) for _ in range(M)]
    edges.sort(key=lambda x:x[2])
    total_weight = 0
    parents = [i for i in range(N+1)]
    for edge in edges:
        u, v, w = edge
        if find(parents, u) != find(parents, v):
            union(parents, u, v)
            total_weight += w
    print(total_weight)