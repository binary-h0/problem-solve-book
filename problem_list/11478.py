# 자료구조, 문자열, 집합과 맵
import sys
input = sys.stdin.readline
s = input().rstrip()

def solve():
    memory = set()
    n = len(s)
    for i in range(1, len(s) + 1):
        j = 0
        while j + i <= n:
            memory.add(s[j:j+i])
            j += 1
    print(len(memory))

if __name__ == '__main__':
    solve()