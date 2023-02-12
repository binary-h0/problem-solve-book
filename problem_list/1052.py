import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().rstrip().split())
    count = 0
    while bin(n).count('1') > k:
        count += 1
        n += 1
    print(count)

if __name__ == '__main__':
    solve()