# 자료구조, 그리디, 정렬, 우선순위 큐
input = __import__('sys').stdin.readline
heap = __import__('heapq')

if __name__ == '__main__':
    n = int(input().rstrip())
    lis = []
    ans = [0 for _ in range(1001)]
    for _ in range(n):
        d, w = map(int, input().rstrip().split())
        heap.heappush(lis, [-w, d])
    for _ in range(n):
        w, d = heap.heappop(lis)
        while 0 < d:
            if ans[d] == 0:
                ans[d] = -w
                break
            else:
                d -= 1
    print(sum(ans))

