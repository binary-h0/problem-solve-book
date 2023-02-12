# 수학
n = int(input())
dp = [0] * (n+1)
dp[1] = 1
if __name__ == '__main__':
    for i in range(2, n+1):
        mini = 4
        j = 1
        while j * j <= i:
            mini = min(mini, dp[i - j * j])
            j += 1
        dp[i] = mini + 1
    print(dp[n])