# 이분 탐색, 두 포인터, 구현
import sys
input = sys.stdin.readline
n = int(input().rstrip())
lis = list(map(int, input().rstrip().split()))
l, r = 0, n-1
ans = [0, n - 1]
while l < r:
    left, right = lis[l], lis[r]
    diff = left + right
    if abs(lis[ans[0]] + lis[ans[1]]) >= abs(diff):
        ans[0], ans[1] = l, r
    if diff > 0:
        r -= 1
    else:
        l += 1
print(lis[ans[0]], lis[ans[1]])