import sys
from collections import deque
input = sys.stdin.readline

def solve(stage, controls):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    que = deque()
    que.append((0, 0))
    n = len(stage)
    direction = 0
    i = 0
    time = 0
    x, command = controls[i]
    while True:
        if time == int(x):
            if command == 'D':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
            i += 1
            if i < len(controls):
                x, command = controls[i]
        r, c = que.pop()
        que.append((r, c))
        nr, nc = r + dx[direction], c + dy[direction]
        if (0 <= nr < n) and (0 <= nc < n):
            if stage[nr][nc] == 2:
                break
            elif stage[nr][nc] == 0:
                r, c = que.popleft()
                stage[r][c] = 0
            que.append((nr, nc))
            stage[nr][nc] = 2
            time += 1
        else:
            break
    print(time+1)

if __name__ == '__main__':
    n = int(input().rstrip())
    stage = [[0 for _ in range(n)] for __ in range(n)]
    stage[0][0] = 2
    k = int(input().rstrip())
    for _ in range(k):
        r, c = map(int, input().rstrip().split())
        stage[r-1][c-1] = 1
    l = int(input().rstrip())
    controls = [tuple(map(str, input().rstrip().split())) for _ in range(l)]
    solve(stage, controls)