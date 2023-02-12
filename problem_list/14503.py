# 구현, 시뮬레이션
import sys
global direction_pointer, r, c, turn_count
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
r, c, d = map(int, input().rstrip().split())
graph = list(list(map(int, input().rstrip().split())) for _ in range(n))
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
direction_pointer = (4 - d) % 4
turn_count = 0

def turnLeft():
    global direction_pointer, turn_count
    direction_pointer = (direction_pointer + 1) % 4
    turn_count += 1

def scanLeft():
    global direction_pointer, r, c
    nr, nc = r + dr[direction_pointer], c + dc[direction_pointer]
    if (0 <= nr < n) and (0 <= nc < m):
        return graph[nr][nc]
    else:
        return 1

def goStraight():
    global direction_pointer, r, c, turn_count
    r += dr[(direction_pointer + 3) % 4]
    c += dc[(direction_pointer + 3) % 4]
    turn_count = 0

def goBack():
    global direction_pointer, r, c, turn_count
    r += dr[(direction_pointer + 1) % 4]
    c += dc[(direction_pointer + 1) % 4]
    turn_count = 0

def scanBehind():
    global direction_pointer, r, c
    nr, nc = r + dr[(direction_pointer + 1) % 4], c + dc[(direction_pointer + 1) % 4]
    if (0 <= nr < n) and (0 <= nc < m):
        return graph[nr][nc]
    else:
        return 1

def solve():
    global r, c, turn_count
    graph[r][c] = 2
    clean_count = 1
    while True:
        result = scanLeft()
        if result == 0:
            turnLeft()
            goStraight()
            graph[r][c] = 2
            clean_count += 1
        elif ((result == 2) or (result == 1)) and turn_count < 4:
            turnLeft()
        elif (turn_count == 4) and (scanBehind() == 1):
            break
        else:
            turn_count = 0
            goBack()
    print(clean_count)

if __name__ == '__main__':
    solve()