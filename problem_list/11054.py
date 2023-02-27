# 다이나믹 프로그래밍
import sys
input = sys.stdin.readline

def solve(n, lis):
    inc = [1 for _ in range(n)]
    dec = [1 for _ in range(n)]
    for i in range(0, n-1):
        for j in range(i+1, n):
            if lis[i] < lis[j]:
                inc[j] = max(inc[i] + 1, inc[j])
            if lis[n - 1 - i] < lis[n - 1 - j]:
                dec[n - 1 - j] = max(dec[n - 1 - j], dec[n - 1 - i] + 1)
    ans = 1
    for i in range(n):
        tmp = inc[i] + dec[i] - 1
        if ans < tmp:
            ans = tmp
    print(ans)

if __name__ == '__main__':
    N = int(input().rstrip())
    lis = list(map(int, input().rstrip().split()))
    solve(N, lis)