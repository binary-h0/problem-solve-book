# 백트래킹
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
lis = sorted(set(map(int, input().rstrip().split())))
stack = []
visited = [False for _ in range(N)]

def solve(n):
    if len(stack) == M:
        print(*stack)
        return
    for i in range(n, len(lis)):
        stack.append(lis[i])
        solve(i)
        stack.pop()

if __name__ == '__main__':
    solve(0)