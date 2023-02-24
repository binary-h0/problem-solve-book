# 다이나믹 프로그래밍, 슬라이딩 윈도우
import sys
input = sys.stdin.readline
N = int(input().rstrip())

def solve():
    a, b, c = map(int, input().rstrip().split())
    min1, min2, min3, max1, max2, max3 = a, b, c, a, b, c
    for _ in range(1, N):
        a, b, c = map(int, input().rstrip().split())
        m1 = min(min1, min2)
        m2 = min(min1, min2, min3)
        m3 = min(min2, min3)
        min1, min2, min3 = a + m1, b + m2, c + m3
        m1 = max(max1, max2)
        m2 = max(max1, max2, max3)
        m3 = max(max2, max3)
        max1, max2, max3 = a + m1, b + m2, c + m3
    print(max(max1, max2, max3), min(min1, min2, min3))

if __name__ == '__main__':
    solve()