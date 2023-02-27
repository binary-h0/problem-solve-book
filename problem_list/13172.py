# 수학, 정수론, 분할 정복, 모듈로 곱셈 역원, 페르마의 소정리
import sys
import math
input = sys.stdin.readline
mod = 1000000007

def solve(n, exp):
    if exp == 1:
        return n
    if exp % 2 == 0:
        tmp = solve(n, exp // 2)
        return tmp * tmp % mod
    else:
        return n * solve(n, exp - 1) % mod

if __name__ == '__main__':
    M = int(input().rstrip())
    ans = 0
    for _ in range(M):
        n, s = map(int, input().rstrip().split())
        gcd = math.gcd(n, s)
        n //= gcd
        s //= gcd

        ans += s * solve(n, mod - 2) % mod
        ans %= mod
    print(ans)