# 자료구조, 해시를 사용한 집합과 맵
import sys
input = sys.stdin.readline

n = int(input())
log = set()
name, state = "", ""
for _ in range(n):
    name, state = input().rstrip().split()
    if state == "enter":
        log.add(name)
    else:
        log.discard(name)
lis = sorted(list(log), reverse=True)
for name in lis:
    print(name)