import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lis = sorted(list(map(int, input().rstrip().split())))
visited = [False for _ in range(n)]
stack = []

def solve(d, n, m):
    if d == m:
        print(' '.join(map(str, stack)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            stack.append(lis[i])
            solve(d + 1, n, m)
            stack.pop()
            visited[i] = False

if __name__ == '__main__':
    solve(0, n, m)