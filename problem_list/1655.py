# 자료구조, 우선순위 큐
input = __import__('sys').stdin.readline
heapq = __import__('heapq')

if __name__ == '__main__':
    lower = []
    upper = []
    tmp = 0
    N = int(input().rstrip())
    n = int(input().rstrip())
    heapq.heappush(lower, -n)
    print(n)
    for _ in range(1, N):
        n = int(input().rstrip())
        if len(lower) > len(upper):
            tmp = -heapq.heappop(lower)
            if tmp <= n:
                heapq.heappush(lower, -tmp)
                heapq.heappush(upper, n)
                print(tmp)
            else:
                heapq.heappush(upper, tmp)
                heapq.heappush(lower, -n)
                tmp2 = -heapq.heappop(lower)
                print(tmp2)
                heapq.heappush(lower, -tmp2)
        else:
            tmp = -heapq.heappop(lower)
            if n <= tmp:
                heapq.heappush(lower, -n)
                print(tmp)
                heapq.heappush(lower, -tmp)
            else:
                tmp2 = heapq.heappop(upper)
                if n < tmp2:
                    print(n)
                    heapq.heappush(lower, -tmp)
                    heapq.heappush(lower, -n)
                    heapq.heappush(upper, tmp2)
                else:
                    print(tmp2)
                    heapq.heappush(lower, -tmp2)
                    heapq.heappush(lower, -tmp)
                    heapq.heappush(upper, n)

        # print(lower, upper)
