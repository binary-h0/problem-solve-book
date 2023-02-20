import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input().rstrip())
chess = [0 for _ in range(n)]
visited = [False for _ in range(n)]
ans = 0

def check(r, c):
    for i in range(0, r):
        if (r - i == abs(chess[i] - c)):
            return False
    return True

def dfs(r):
    global ans
    if r == n:
        ans += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        if check(r, i):
            chess[r] = i
            visited[i] = True
            dfs(r + 1)
            visited[i] = False

def solve():
    dfs(0)
    print(ans)

if __name__ == '__main__':
    solve()
