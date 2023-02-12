# 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline

def solve(c):
    global x, y, visited
    que = deque()
    que.append((x, ''))
    while len(que) > 0:
        n, s = que.popleft()
        # print(n, s)
        if n == y:
            print(s)
            return
        tmp = (n * 2) % 10000
        if visited[tmp] != c:
            que.append((tmp, s+'D'))
            visited[tmp] = c
        tmp = 9999 if (n-1) == -1 else (n - 1)
        if visited[tmp] != c:
            que.append((tmp, s + 'S'))
            visited[tmp] = c
        tmp = (n % 1000)*10 + n // 1000
        if visited[tmp] != c:
            que.append((tmp, s + 'L'))
            visited[tmp] = c
        tmp = (n % 10) * 1000 + (n - (n % 10)) // 10
        if visited[tmp] != c:
            que.append((tmp, s + 'R'))
            visited[tmp] = c



if __name__ == '__main__':
    visited = [0 for _ in range(10000)]
    for _ in range(1, int(input().rstrip()) + 1):
        x, y = map(int, input().rstrip().split())
        solve(_)
