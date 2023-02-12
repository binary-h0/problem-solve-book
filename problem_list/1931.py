# 그리디, 정렬
import sys
input = sys.stdin.readline

n = int(input().rstrip())
schedule = []
for _ in range(n):
    ans = 0
    start, end = map(int, input().rstrip().split())
    schedule.append((start, end))
schedule.sort(key=lambda x: x[1])
schedule.sort(key=lambda x: x[0])
s, e = schedule[0]
print(schedule)
for i in range(1, n):
    ts, te = schedule[i]
    if te < e:
        e = te
        s = ts
        print(s, e)
        continue
    if e <= ts:
        e = te
        s = ts
        ans += 1
        print(s, e)
print(ans + 1)

