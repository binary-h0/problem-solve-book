# 자료구조, 그리디, 우선순위 큐
input = __import__('sys').stdin.readline
heap = __import__('heapq')

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    cards = []
    for i in list(map(int, input().rstrip().split())):
        heap.heappush(cards, i)
    for _ in range(m):
        card1 = heap.heappop(cards)
        card2 = heap.heappop(cards)
        tmp = card1 + card2
        heap.heappush(cards, tmp)
        heap.heappush(cards, tmp)
    print(sum(cards))