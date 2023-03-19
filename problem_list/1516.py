# 위상 정렬, 다이나믹 프로그래밍, 그래프 이론
import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
graph = [[] for _ in range(N+1)]
times = [0 for _ in range(N+1)]
raw = []
ans = [0 for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
for i in range(1, N+1):
    lis = list(map(int, input().rstrip().split()))
    raw.append(lis[1:len(lis)-1])
    times[i] = lis[0]
    for n in range(1, len(lis) - 1):
        graph[lis[n]].append(i)
        degrees[i] += 1

def solve():
    que = deque()
    topology = [[] for _ in range(N)]

    for i in range(1, N+1):
        if degrees[i] == 0:
            que.append((i, 0))
    while que:
        n, w = que.popleft()
        topology[w].append(n)
        for next in graph[n]:
            degrees[next] -= 1
            if degrees[next] == 0:
                que.append((next, w + 1))
    for i in range(N):
        if len(topology[i]) == 0:
            break
        for j in topology[i]:
            if len(raw[j-1]) == 0:
                ans[j] = times[j]
            else:
                ans[j] = times[j] + max(list(times[x] for x in raw[j - 1]))
            times[j] = ans[j]
    for i in range(1, N+1):
        print(times[i])

if __name__ == '__main__':
    solve()