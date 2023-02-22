import sys
import heapq
input = sys.stdin.readline

def solve():
    heap = []
    n = int(input().rstrip())
    for _ in range(n):
        for i in list(map(int, input().rstrip().split())):
            if len(heap) < n:
                heapq.heappush(heap, i)
            else:
                if heap[0] < i:
                    heapq.heappop(heap)
                    heapq.heappush(heap, i)
    print(heap[0])

if __name__ == '__main__':
    solve()