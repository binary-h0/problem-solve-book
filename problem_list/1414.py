import sys
input = sys.stdin.readline
N = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(N)]
parents = [i for i in range(N+1)]
edges = []
ans = 0
for r in range(N):
    for c in range(N):
        line = ord(graph[r][c])
        if 96 < line < 123:
            ans += line - 96
            edges.append((r, c, line - 96))
            # edges.append((c, r, line - 96))
        elif 64 < line < 91:
            ans += line - 38
            edges.append((r, c, line - 38))
            # edges.append((c, r, line - 38))
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
    connected = 1
    for edge in edges:
        a, b, w = edge
        if find(a) != find(b):
            union(a, b)
            ans -= w
            connected += 1
    if connected == N:
        print(ans)
    else:
        print(-1)