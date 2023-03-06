import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
s, e = map(int, input().rstrip().split())
edges = [tuple(map(int, input().rstrip().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2], reverse=True)
parents = [i for i in range(N+1)]
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

ans = 999999999999999
if __name__ == '__main__':
    flag = True
    for edge in edges:
        x, y, w = edge
        if find(x) != find(y):
            union(x, y)
            ans = min(ans, w)
            if find(s) == find(e):
                print(ans)
                flag = False
                break
    if flag:
        print(0)