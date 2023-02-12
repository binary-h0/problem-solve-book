import sys
input = sys.stdin.readline

def tetromino_I(N, M, arr):
    ans = 0
    for i in range(N):
        for j in range(M - 3):
            sum = 0
            for k in range(j, j + 4):
                sum += arr[i][k]
            ans = max(ans, sum)

    for i in range(N - 3):
        for j in range(M):
            sum = 0
            for k in range(i, i + 4):
                sum += arr[k][j]
            ans = max(ans, sum)

    return ans


def tetromino_LTZr(N, M, arr):
    ans = 0
    for i in range(N - 1):
        for j in range(M - 2):
            sum_L = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 2]
            sum_ㅏ = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1]
            sum_r = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j]
            sum_tN = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
            ans = max(ans, sum_L, sum_ㅏ, sum_r, sum_tN)

    for i in range(1, N):
        for j in range(M - 2):
            sum_J = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i - 1][j + 2]
            sum_ㅓ = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i - 1][j + 1]
            sum_ㄱ = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i - 1][j]
            sum_N = arr[i][j] + arr[i][j + 1] + arr[i - 1][j + 1] + arr[i - 1][j + 2]
            ans = max(ans, sum_J, sum_ㅓ, sum_ㄱ, sum_N)

    for i in range(N - 2):
        for j in range(M - 1):
            sum_ㄱ = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1]
            sum_ㅜ = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 1][j + 1]
            sum_r = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i][j + 1]
            sum_Z = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
            ans = max(ans, sum_ㄱ, sum_ㅜ, sum_r, sum_Z)

    for i in range(N - 2):
        for j in range(1, M):
            sum_J = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j - 1]
            sum_ㅗ = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 1][j - 1]
            sum_ㄴ = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i][j - 1]
            sum_tZ = arr[i][j] + arr[i + 1][j] + arr[i + 1][j - 1] + arr[i + 2][j - 1]
            ans = max(ans, sum_J, sum_ㅗ, sum_ㄴ, sum_tZ)

    return ans


def tetromino_ㅁ(N, M, arr):
    ans = 0
    for i in range(N - 1):
        for j in range(M - 1):
            sum = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
            ans = max(ans, sum)

    return ans


N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

print(max(tetromino_I(N, M, arr), tetromino_LTZr(N, M, arr), tetromino_ㅁ(N, M, arr)))