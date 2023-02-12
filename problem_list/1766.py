# 자료구조, 그래프 이론, 우선순위 큐, 위상 정렬
input = __import__('sys').stdin.readline
heap = __import__('heapq')

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    graph = [[] for _ in range(n+1)]
    degree = [0 for _ in range(n+1)]
    que = []
    ans = []

    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        degree[b] += 1

    for i in range(1, n+1):
        if degree[i] == 0:
            heap.heappush(que, i)

    while que:
        tmp = heap.heappop(que)
        ans.append(tmp)
        for i in graph[tmp]:
            degree[i] -= 1
            if degree[i] == 0:
                heap.heappush(que, i)

    print(*ans)