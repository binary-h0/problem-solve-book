# 수학, 정수론, 중국인의 나머지 정리
import sys
input = sys.stdin.readline

def solve(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

if __name__ == '__main__':
    for _ in range(int(input().rstrip())):
        m, n, x, y = map(int, input().rstrip().split())
        print(solve(m, n, x, y))