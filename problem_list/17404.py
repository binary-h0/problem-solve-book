# 다이나믹 프로그래밍
import sys
def solve():
    input = sys.stdin.readline
    n = int(input().rstrip())
    rgb_lis = [list(map(int, input().rstrip().split())) for _ in range(n)]
    memory = [[0] * 3 for _ in range(n)]
    inf = 100000000
    ans = inf
    memory[0][0], memory[0][1], memory[0][2] = inf, rgb_lis[0][1], rgb_lis[0][2]
    for i in range(1, n):
        memory[i][0] = min(memory[i - 1][1], memory[i - 1][2]) + rgb_lis[i][0]
        memory[i][1] = min(memory[i - 1][0], memory[i - 1][2]) + rgb_lis[i][1]
        memory[i][2] = min(memory[i - 1][1], memory[i - 1][0]) + rgb_lis[i][2]
    ans = min(ans, memory[n - 1][0])
    memory[0][0], memory[0][1], memory[0][2] = rgb_lis[0][0], inf, rgb_lis[0][2]
    for i in range(1, n):
        memory[i][0] = min(memory[i - 1][1], memory[i - 1][2]) + rgb_lis[i][0]
        memory[i][1] = min(memory[i - 1][0], memory[i - 1][2]) + rgb_lis[i][1]
        memory[i][2] = min(memory[i - 1][1], memory[i - 1][0]) + rgb_lis[i][2]
    ans = min(ans, memory[n - 1][1])
    memory[0][0], memory[0][1], memory[0][2] = rgb_lis[0][0], rgb_lis[0][1], inf
    for i in range(1, n):
        memory[i][0] = min(memory[i - 1][1], memory[i - 1][2]) + rgb_lis[i][0]
        memory[i][1] = min(memory[i - 1][0], memory[i - 1][2]) + rgb_lis[i][1]
        memory[i][2] = min(memory[i - 1][1], memory[i - 1][0]) + rgb_lis[i][2]
    ans = min(ans, memory[n - 1][2])
    print(ans)

if __name__ == '__main__':
    solve()