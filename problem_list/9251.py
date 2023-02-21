# LCS
import sys
input = sys.stdin.readline
b = input().rstrip()
a = input().rstrip()

def solve():
    graph = [[0 for _ in range(len(a) + 1)] for __ in range(len(b) + 1)]
    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            if b[i - 1] == a[j - 1]:
                graph[i][j] = graph[i - 1][j - 1] + 1
            else:
                graph[i][j] = max(graph[i][j - 1], graph[i - 1][j])
    print(graph[-1][-1])

if __name__ == '__main__':
    solve()
