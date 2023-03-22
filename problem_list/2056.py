# 다이나믹 프로그래밍, 그래프 이론, 위상 정렬
n = int(input())
dp = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    cost, m, *lst = map(int, input().split())
    dp[i] = cost
    for x in lst:
        graph[i].append(x)

for i in range(1, n+1):
    tmp = 0
    for j in graph[i]:
        tmp = max(tmp, dp[j])
    dp[i] += tmp
print(max(dp))