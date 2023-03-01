# 수학, 그리디
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip().split())
    pack, single = 9999999999, 9999999999
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        if a < pack:
            pack = a
        if b < single:
            single = b
    t2 = 9999999999
    if N % 6 == 0:
        t1 = N // 6
    else:
        t1 = (N // 6) + 1
        t2 = (N % 6) * single + (t1 - 1) * pack
    t1 = t1 * pack
    t3 = N * single
    print(min(t1, t2, t3))
main()