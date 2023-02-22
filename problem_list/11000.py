import sys
import heapq
input = sys.stdin.readline
n = int(input().rstrip())
heap = []
for _ in range(n):
    s, e = map(int, input().rstrip().split())
    heapq.heappush(heap, (s, e))

def solve():
    ans = 0
    que = []
    s, e = heapq.heappop(heap)
    heapq.heappush(que, e)
    while heap:
        ns, ne = heapq.heappop(heap)
        if ns < que[0]:
            if ne <= que[0]:
                heapq.heappush(que, ne)
        else:
            while que:
                e = heapq.heappop(que)
                if e > ns:
                    heapq.heappush(que, e)
                    break
            heapq.heappush(que, ne)
        print(que)
        if ans < len(que):
            ans = len(que)
    print(ans)


if __name__ == '__main__':
    solve()
