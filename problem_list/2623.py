# 그래프 이론, 위상 정렬
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
degrees = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
mem = set()
for _ in range(M):
    lis = list(map(int, input().rstrip().split()))
    for i in range(1, len(lis)-1):
        a, b = lis[i], lis[i+1]
        if (a, b) in mem:
            continue
        mem.add((a, b))
        graph[a].append(b)
        degrees[b] += 1

def solve():
    que = deque()
    stack = []
    for i in range(1, N+1):
        if degrees[i] == 0:
            que.append(i)
    while que:
        n = que.popleft()
        stack.append(n)
        for next in graph[n]:
            degrees[next] -= 1
            if degrees[next] == 0:
                que.append(next)
    if len(stack) != N:
        print(0)
    else:
        for s in stack:
            print(s)

if __name__ == '__main__':
    solve()
