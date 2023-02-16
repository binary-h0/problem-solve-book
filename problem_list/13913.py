# 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline

def solve(visited, n, k):
    visited[n] = True
    memory = [-1 for _ in range(150001)]
    que = deque()
    que.append((n, 0))
    while que:
        x, t = que.popleft()
        if x == k:
            s = []
            print(t)
            while memory[k] != -1:
                s.append(k)
                k = memory[k]
            s.append(n)
            print(*s[::-1])
            return
        for nx in [x + 1, x - 1, x * 2]:
            if (0 <= nx < 150001):
                if not visited[nx]:
                    memory[nx] = x
                    que.append((nx, t+1))
                    visited[nx] = True

if __name__ == '__main__':
    N, K = map(int, input().rstrip().split())
    visited = [False for _ in range(150001)]
    solve(visited, N, K)