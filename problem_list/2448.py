# 재귀
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
graph = [['' for _ in range(n*2)] for __ in range(n)]

def solve(n, r, c):
    if n == 3:
        graph[r][c + 2] = '*'
        graph[r + 1][c + 1], graph[r + 1][c + 3] = '*', '*'
        for i in range(5):
            graph[r + 2][c + i] = '*'
        return
    solve(n // 2, r + (n // 2), c)
    solve(n // 2, r + (n // 2), c + n)
    solve(n // 2, r , c + (n // 2))

if __name__ == '__main__':
    solve(n, 0, 0)
    for r in range(n):
        for c in range(n*2):
            if graph[r][c] == '*':
                print('*')
            else:
                print(' ')
        print('\n')