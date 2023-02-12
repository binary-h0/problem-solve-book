# 자료구조, 그리디, 우선순위 큐
input = __import__('sys').stdin.readline
heap = __import__('heapq')

if __name__ == '__main__':
    cards = []
    a1 = 0
    a2 = 0
    ans = 0
    for _ in range(int(input().rstrip())):
        heap.heappush(cards, int(input().rstrip()))

    combCards = []
    while True:
        if len(cards) >= 2 :
            a1 = heap.heappop(cards)
            a2 = heap.heappop(cards)
            tmp = a1 + a2
            ans += tmp
            heap.heappush(cards, tmp)
        else:
            break
    print(ans)
