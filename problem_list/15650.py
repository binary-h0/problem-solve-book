# 백트래킹
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
stack = []

def solve(start):
    if len(stack) == M:
        print(' '.join(map(str, stack)))
    for i in range(start, N + 1):
        if i not in stack:
            stack.append(i)
            solve(i+1)
            stack.pop()

if __name__ == '__main__':
    solve(1)