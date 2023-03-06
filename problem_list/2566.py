import sys
input = sys.stdin.readline
arr = [list(map(int, input().rstrip().split())) for _ in range(9)]
max_n = 0
ans = [1, 1]
for r in range(9):
    for c in range(9):
        if max_n < arr[r][c]:
            max_n = arr[r][c]
            ans[0], ans[1] = r+1, c+1
print(max_n)
print(*ans)