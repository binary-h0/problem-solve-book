# 수학, 구현, 사칙연산
import sys
input = sys.stdin.readline

x = int(input().rstrip())
n = int(input().rstrip())
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    x -= a * b
if x == 0:
    print("Yes")
else:
    print("No")