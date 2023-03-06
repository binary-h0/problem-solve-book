# 그래프 이론, 최소 스패닝 트리
import sys
input = sys.stdin.readline

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    x, y = find(parents, x), find(parents, y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def main(m, n):
    parents = [i for i in range(m + 1)]
    edges = []
    ans = 0
    for _ in range(n):
        x, y, z = map(int, input().rstrip().split())
        edges.append((z, x, y))
        ans += z
    edges.sort()
    for edge in edges:
        w, u, v = edge
        if find(parents, u) != find(parents, v):
            union(parents, u, v)
            ans -= w
    print(ans)

if __name__ == '__main__':
    while 1:
        m, n = map(int, input().rstrip().split())
        if m == 0 and n == 0:
            break
        main(m, n)
