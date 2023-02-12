import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    lis = [[1 for _ in range(101)] for _ in range(101)]
    for i in range(1, n+1):
        for j in range(1, i):
            lis[i][j] = lis[i-1][j-1] + lis[i-1][j]
    print(lis[n][m])