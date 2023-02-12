# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 플로이드-워셜
import sys
from collections import deque
input = sys.stdin.readline

def solve(n):
    global graph, minCount
    visited = [0 for _ in range(101)]
    que = deque()
    que.append(n)
    visited[n] += 1
    piv = 0
    ans = 0
    while len(que) > 0:
        num = que.popleft()
        piv = visited[num]
        for i in graph[num]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = 1 + piv
                ans += visited[i]
        if piv > minCount:
            return 99999999
    return ans

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    graph = [[] for _ in range(n+1)]
    minCount = 999999999
    nodeNum = 101
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n+1):
        maxCount = solve(i)
        if minCount > maxCount:
            minCount = maxCount
            nodeNum = i
    print(nodeNum)