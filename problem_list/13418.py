# 그래프 이론, 최소 스패닝 트리
import sys
input = sys.stdin.readline

def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)
    return parents[x]
def union(x, y, parents):
    x, y = find(x, parents), find(y, parents)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
def solve():
    N, M = map(int, input().rstrip().split())
    edges = [tuple(map(int, input().rstrip().split())) for _ in range(M + 1)]
    parents = [i for i in range(N + 1)]
    min_total, max_total = 0, 0
    edges.sort(key=lambda x: x[2])
    for i in range(M+1):
        a, b, c = edges[i]
        if find(a, parents) != find(b, parents):
            union(a, b, parents)
            if c == 0:
                min_total += 1
    min_total = min_total ** 2
    parents = [i for i in range(N + 1)]
    for i in range(M, -1, -1):
        a, b, c = edges[i]
        if find(a, parents) != find(b, parents):
            union(a, b, parents)
            if c == 0:
                max_total += 1
    max_total = max_total ** 2
    print(min_total - max_total)

if __name__ == '__main__':
    solve()