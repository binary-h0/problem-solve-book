# 분할 정복, 재귀
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def solve(n, x, y):
    global blue, white
    if n == 1:
        if paper[x][y]:
            blue += 1
        else:
            white += 1
        return paper[x][y]
    else:
        next_n = n >> 1
        totalNum = 0
        totalNum += solve(next_n, x, y)
        totalNum += solve(next_n, x, y + next_n)
        totalNum += solve(next_n, x + next_n, y)
        totalNum += solve(next_n, x + next_n, y + next_n)

        if n * n == totalNum:
            blue -= 3
        elif totalNum == 0:
            white -= 3

        return totalNum


if __name__ == '__main__':
    n = int(input().rstrip())
    paper = [list(map(int, input().rstrip().split())) for _ in range(n)]
    blue = 0
    white = 0

    solve(n, 0, 0)
    print(white)
    print(blue)