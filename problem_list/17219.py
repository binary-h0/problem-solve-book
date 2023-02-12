# 자료구조, 해시를 이용한 집합과 맵
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    passwords = dict()
    for _ in range(n):
        s, p = map(str, input().rstrip().split())
        passwords[s] = p
    for _ in range(m):
        print(passwords[input().rstrip()])