lis = [500, 100, 50, 10, 5, 1]
n = 1000 - int(input())
ans = 0
for i in range(6):
    if n >= lis[i]:
        ans += n // lis[i]
        n %= lis[i]
print(ans)