# 백트래킹
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
lis = list(map(int, input().rstrip().split()))
lis.sort()
stack = []

def solve(n):
    if len(stack) == M:
        print(*stack)
        return

    for i in range(n, N):
        stack.append(lis[i])
        solve(i)
        stack.pop()

if __name__ == '__main__':
    solve(0)