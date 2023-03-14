import sys
input = sys.stdin.readline
N, M, K = map(int, input().rstrip().split())
lis = list(map(int, input().rstrip().split()))
parents = [i for i in range(N+1)]
for i in lis:
    parents[i] = 0
edges = []
for _ in range(M):
    u, v, w = map(int, input().rstrip().split())
    edges.append((u, v, w))
edges.sort(key=lambda x:x[2])

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

if __name__ == '__main__':
    ans = 0
    for edge in edges:
        a, b, w = edge
        if find(a) != find(b):
            union(a, b)
            ans += w
    print(ans)