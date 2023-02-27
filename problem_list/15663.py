# 백트래킹
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
lis = sorted(list(map(int, input().rstrip().split())))
stack = []
visited = [False for _ in range(N)]

def solve():
    if len(stack) == M:
        print(*stack)
        return
    tmp = 0
    for i in range(N):
        if tmp == lis[i] :
            continue
        if visited[i]:
            continue
        visited[i] = True
        stack.append(lis[i])
        tmp = lis[i]
        solve()
        visited[i] = False
        stack.pop()

if __name__ == '__main__':
    solve()