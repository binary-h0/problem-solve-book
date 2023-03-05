import sys, math
from itertools import combinations
input = sys.stdin.readline

def solve(n, coords):
    x_total, y_total = 0, 0
    for x, y in coords:
        x_total += x
        y_total += y
    ans = math.inf
    comb = list(combinations(coords, n // 2))
    for coord in comb[:len(comb)//2]:
        x_t, y_t = 0, 0
        for x, y in coord:
            x_t += x
            y_t += y
        x, y = x_total - x_t, y_total - y_t
        ans = min(ans, math.sqrt((x_t - x)**2 + (y_t - y)**2))
    return ans

def main():
    n = int(input().rstrip())
    coords = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
    print(solve(n, coords))

if __name__ == '__main__':
    for _ in range(int(input().rstrip())):
        main()

