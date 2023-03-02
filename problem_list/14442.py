import sys
from collections import deque

dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def solution(N, M, K, board):
    if N == 1 and M == 1:
        return 1

    visited = [[K + 1] * M for _ in range(N)]
    visited[0][0] = 0
    queue = deque([(0, 0, 1)])
    while queue:
        x, y, d = queue.popleft()
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if (nx, ny) == (M - 1, N - 1):
                return d + 1
            k = board[ny][nx] + visited[y][x]
            if k < visited[ny][nx] and k <= K:
                visited[ny][nx] = k
                queue.append((nx, ny, d + 1))
    return -1


IN, IM, IK = map(int, sys.stdin.readline().split())
IBoard = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(IN)]
print(solution(IN, IM, IK, IBoard))