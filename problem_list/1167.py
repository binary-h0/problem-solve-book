# 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solve(n, c):
    visited[n] = True
    flag = True
    max_cost = 0
    lis = []
    for next_node, next_cost in graph[n]:
        if not visited[next_node]:
            flag = False
            cost = solve(next_node, c + next_cost)
            if c == 0:
                lis.append(cost)
            if max_cost < cost:
                max_cost = cost
    if flag:
        return c
    if c == 0:
        if len(lis) == 1:
            print(*lis)
        else:
            lis.sort()
            print(lis[len(lis) - 1] + lis[len(lis) - 2])
    return max_cost

if __name__ == '__main__':
    N = int(input().rstrip())
    graph = [[] for _ in range(0, N + 1)]
    ans = 0
    visited = [False for _ in range(N + 1)]
    for _ in range(N):
        lis = list(map(int, input().rstrip().split()))
        node = lis[0]
        i = 1
        while lis[i] != -1:
            graph[node].append((lis[i], lis[i + 1]))
            i += 2
    solve(1, 0)
