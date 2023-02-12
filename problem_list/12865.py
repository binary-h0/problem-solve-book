# 다이나믹 프로그래밍, 배낭 문제
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().rstrip().split())
    lis = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
    lis.sort()
    memory = [0 for _ in range(k + 1)]
    for i in range(n):
        w, v = lis[i]
        memory[w] = v

    tmp = memory[0]
    w = 0
    for j in range(1, k + 1):
        memory[j] = max(tmp, memory[j])