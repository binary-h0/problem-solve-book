# 그리디
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().rstrip().split())
    coins = []
    ptr = n-1
    ans = 0
    for _ in range(n):
        coins.append(int(input().rstrip()))
    while k != 0:
        if coins[ptr] <= k:
            ans += k // coins[ptr]
            k %= coins[ptr]
        else:
            ptr -= 1
    print(ans)