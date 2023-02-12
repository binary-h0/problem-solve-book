# 수학, 다이나믹 프로그래밍

if __name__ == '__main__':
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        ans = (ans + k) % i
    print(ans + 1)