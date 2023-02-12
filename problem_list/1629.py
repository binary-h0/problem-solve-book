# 수학, 분할 정복
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    a, b, c = map(int, input().rstrip().split())
    res = 1
    while b:
        if b & 1:
            res = (res * a) % c
        a = (a * a) % c
        b >>= 1
    print(res)