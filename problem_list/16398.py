# 그래프 이론, 최소 스패닝 트리
import sys
input = sys.stdin.readline
n = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
parents = [i for i in range(n)]
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
edges = []
for r in range(n-1):
    for c in range(r + 1, n):
        edges.append((graph[r][c], r, c))
edges.sort()
ans = 0
for edge in edges:
    w, u, v = edge
    if find(u) != find(v):
        union(u, v)
        ans += w
print(ans)