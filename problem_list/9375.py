# 수학, 자료구조, 조합론, 해시를 사용한 집합과 맵
import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    s = set()
    for __ in range(int(input().rstrip())):
        a, b = map(str, input().rstrip().split())
        s.add(a)
        s.add(b)