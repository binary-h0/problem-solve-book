# 그래프 이론, 최소 스패닝 트리, 정렬
import sys
input = sys.stdin.readline
n = int(input().rstrip())
parents = [i for i in range(n)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]
def union(x, y):
    parents_x = find(x)
    parents_y = find(y)
    if parents_x < parents_y:
        parents[parents_y] = parents_x
    else:
        parents[parents_x] = parents_y

def solve():
    xlis, ylis, zlis = [], [], []
    for i in range(n):
        x, y, z = map(int, input().rstrip().split())
        xlis.append((x, i))
        ylis.append((y, i))
        zlis.append((z, i))
    xlis.sort()
    ylis.sort()
    zlis.sort()
    edges = []
    for lis in xlis, ylis, zlis:
        for i in range(1, n):
            w1, u = lis[i - 1]
            w2, v = lis[i]
            edges.append((abs(w1 - w2), u, v))
    edges.sort()
    total_weight = 0
    for edge in edges:
        w, u, v = edge
        if find(u) != find(v):
            union(u, v)
            total_weight += w
    print(total_weight)

if __name__ == '__main__':
    solve()