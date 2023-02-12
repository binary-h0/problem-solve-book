# 구현, 자료구조, 시뮬레이션, 스택
import sys
input = sys.stdin.readline
n = int(input())
unwashed = [i for i in range(n, 0, -1)]
washed = []
dried = []

while (len(dried) != n):
    c, d = map(int, input().split())
    if c == 1:
        for _ in range(d):
            washed.append(unwashed.pop())
    else:
        for _ in range(d):
            dried.append(washed.pop())

for i in range(n-1, -1, -1):
    print(dried[i])