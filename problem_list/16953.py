# 그래프 이론, 그리디, 그래프 탐색, 너비우선탐색
from collections import deque

def bfs(start):
    global visited, answer, b
    que = deque()
    que.append((start, 1))

    while que:
        number, count = que.popleft()
        if number == b:
            answer = count
            break
        next_number = number * 2
        if next_number > b:
            continue
        que.append((next_number, count + 1))

        next_number = number * 10 + 1
        if next_number > b:
            continue
        que.append((next_number, count + 1))


if __name__ == '__main__':
    a, b = map(int, input().split())
    answer = -1
    bfs(a)
    print(answer)