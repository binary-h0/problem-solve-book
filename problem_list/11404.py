import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
dist = [[float('inf') for _ in range(n)] for __ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, d = map(int, input().rstrip().split())
    if dist[a-1][b-1] < d:
        continue
    dist[a-1][b-1] = d

def floyd_warshall():
    for k in range(n):
        for a in range(n):
            for b in range(n):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])
    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                dist[i][j] = 0
    for i in dist:
        print(*i)

if __name__ == '__main__':
    floyd_warshall()