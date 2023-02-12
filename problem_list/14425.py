# 자료구조, 문자열, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = set()
ret = 0
for _ in range(n):
    s.add(input().rstrip())

for _ in range(m):
    if input().rstrip() in s:
        ret += 1
print(ret)