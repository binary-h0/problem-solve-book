# 분할 정복, 재귀
import sys
sys.setrecursionlimit(10**9)
input = __import__('sys').stdin.readline

zero = 0
plus = 0
minus = 0

def solve(n, x, y):
    global zero, plus, minus
    if n == 1:
        if paper[x][y] == 1:
            plus += 1
        elif paper[x][y] == -1:
            minus += 1
        else:
            zero += 1
        return paper[x][y]

    pivot = paper[x][y]
    flag = True
    for i in range(3):
        for j in range(3):
            ret = solve(n // 3, ((n // 3) * i) + x, ((n // 3) * j) + y)
            # print(zero, plus, minus, flag, ((n // 3) * i) + x, ((n // 3) * j) + y)
            if not ret == pivot:
                flag = False
                # break

    if flag:
        if pivot == 1:
            plus -= 8
        elif pivot == -1:
            minus -= 8
        elif pivot == 0:
            zero -= 8
        return pivot
    else:
        return 2

if __name__ == '__main__':

    n = int(input())
    paper = [ list(map(int, input().rstrip().split())) for _ in range(n)]
    solve(n, 0, 0)
    print(minus)
    print(zero)
    print(plus)
