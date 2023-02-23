# 다이나믹 프로그래밍
import sys
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())
    memory = [list(map(int, input().rstrip().split())) for __ in range(2)]
    if n == 1:
        print(max(memory[0][0], memory[1][0]))
    elif n == 2:
        print(max(memory[0][0] + memory[1][1], memory[1][0] + memory[0][1]))
    else:
        memory[0][1] += memory[1][0]
        memory[1][1] += memory[0][0]
        for i in range(2, n):
            memory[0][i] += max(memory[1][i-1], memory[1][i-2])
            memory[1][i] += max(memory[0][i-1], memory[0][i-2])
        print(max(memory[0][n-1], memory[1][n-1]))

if __name__ == '__main__':
    for _ in range(int(input().rstrip())):
        solve()