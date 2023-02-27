import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    lis = []
    for _ in range(n):
        x, y = map(int, input().rstrip().split())
        lis.append((x, y))
    max_n, min_n = float('-inf'), float('inf')
    for x, y in lis:
        max_n = max(max_n, x+y)
        min_n = min(min_n, x+y)
    ans1 = max_n - min_n
    max_n, min_n = float('-inf'), float('inf')
    for x, y in lis:
        max_n = max(max_n, x - y)
        min_n = min(min_n, x - y)
    ans2 = max_n - min_n
    print(max(ans1, ans2))
main()