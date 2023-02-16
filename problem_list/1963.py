# 수학, 그래프 이론 그래프 탐색, 정수론, 너비 우선 탐색, 소수 판정, 에라토스테네스의 체
import sys
from collections import deque
input = sys.stdin.readline

def getNumList(n):
    lis = [n // 1000, (n % 1000) // 100, (n % 100) // 10, n % 10]
    mem = lis[:]
    ret = []
    for i in range(1, 10):
        lis[0] = i
        ret.append(lis[0] * 1000 + lis[1] * 100 + lis[2] * 10 + lis[3])

    for j in range(1, 4):
        lis = mem[:]
        for i in range(0, 10):
            lis[j] = i
            ret.append(lis[0] * 1000 + lis[1] * 100 + lis[2] * 10 + lis[3])
    return ret

def solve(primes, a, b):
    visited = [False for _ in range(10000)]
    visited[a] = True
    que = deque()
    que.append((a, 0))
    while que:
        n, c = que.popleft()
        if n == b:
            print(c)
        for nn in getNumList(n):
            if visited[nn]:
                continue
            if primes[nn]:
                que.append((nn, c + 1))
                visited[nn] = True

if __name__ == '__main__':
    primes = [True for _ in range(10000)]
    primes[0], primes[1] = False, False
    for i in range(2, 10000):
        if primes[i] == False:
            continue
        else:
            for j in range(i*2, 10000, i):
                primes[j] = False
    for _ in range(int(input().rstrip())):
        a, b = map(int, input().rstrip().split())
        solve(primes, a, b)