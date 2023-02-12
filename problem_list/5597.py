# 구현
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    lis = [False for _ in range(31)]
    for _ in range(28):
        lis[int(input().rstrip())] = True
    for i in range(1, 31):
        if not lis[i]:
            print(i)