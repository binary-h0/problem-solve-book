# 그래프 이론, 위상 정렬
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
topology = [0 for i in range(N+1)]
que = deque()
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    topology[b] += 1

for i in range(1, N+1):
    if topology[i] == 0:
        que.append(i)
def solve():
    ans = []
    while que:
        n = que.popleft()
        ans.append(n)
        for i in graph[n]:
            topology[i] -= 1
            if topology[i] == 0:
                que.append(i)
    print(*ans)

if __name__ == '__main__':
    solve()