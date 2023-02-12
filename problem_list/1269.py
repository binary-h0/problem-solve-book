# 해시를 이용한 집합과 맵
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    _, __ = map(int, input().rstrip().split())
    a = set(map(int, input().rstrip().split()))
    b = set(map(int, input().rstrip().split()))
    print(len(a.difference(b)) + len(b.difference(a)))