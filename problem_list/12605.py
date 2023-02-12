# 자료구조, 문자열, 파싱, 스택
import sys
input = sys.stdin.readline

n = 1
for _ in range(int(input())):
    case_str = list(input().split())
    print("Case #{}: ".format(n), end="")
    for i in range(1, len(case_str)):
        print(case_str[len(case_str) - i], end=" ")
    print(case_str[0])
    n += 1