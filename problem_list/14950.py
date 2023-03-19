import sys
input = sys.stdin.readline
N, M, t = map(int, input().rstrip().split())
parants = [i for i in range(N+1)]
edges = []
for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    edges.append((a, b, c))
edges.sort(key=lambda x:x[2])

def find(x):
    if parants[x] != x:
        parants[x] = find(parants[x])
    return parants[x]
def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parants[y] = x
    else:
        parants[x] = y
if __name__ == '__main__':
    ans = t * (N-2) * (N-1) // 2
    for edge in edges:
        a, b, c = edge
        if find(a) != find(b):
            union(a, b)
            ans += c
    print(ans)