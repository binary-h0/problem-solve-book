# 다이나믹 프로그래밍, 그래프 이론, 위상 정렬
from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().rstrip().split())
    times = list(map(int, input().rstrip().split()))
    graph = [[] for _ in range(N)]
    in_degree = [0 for _ in range(N)]
    memory = [0 for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().rstrip().split())
        in_degree[b-1] += 1
        graph[a-1].append(b-1)
    W = int(input().rstrip())
    que = deque()
    for i in range(N):
        if in_degree[i] == 0:
            que.append(i)
        memory[i] = times[i]
    while que:
        node = que.popleft()
        t = memory[node]
        for next_node in graph[node]:
            in_degree[next_node] -= 1
            memory[next_node] = max(memory[next_node], t + times[next_node])
            if in_degree[next_node] == 0:
                que.append(next_node)
    print(memory[W-1])

for _ in range(int(input().rstrip())):
    main()