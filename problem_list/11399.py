# 그리디, 정렬
import sys
input = sys.stdin.readline

n = int(input().rstrip())
peoples = list(map(int, input().rstrip().split()))
peoples.sort()

ans = 0
for i in range(n, 0, -1):
    ans += peoples[n - i] * i
print(ans)