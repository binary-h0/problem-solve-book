# 자료구조, 그리디, 정렬, 우선순위 큐
input = __import__('sys').stdin.readline
heap = __import__('heapq')

if __name__ == '__main__':
    bags = []
    jewelrys = []
    goodJewelry = []
    n, k = map(int, input().rstrip().split())
    ans = 0
    for _ in range(n):
        heap.heappush(jewelrys, list(map(int, input().rstrip().split())))
    for _ in range(k):
        heap.heappush(bags, int(input().rstrip()))
    for _ in range(len(bags)):
        bag = heap.heappop(bags)
        while len(jewelrys) > 0:
            weight, price = heap.heappop(jewelrys)
            if weight <= bag:
                heap.heappush(goodJewelry, [-price, weight])
            else:
                heap.heappush(jewelrys, [weight, price])
                break
        if len(goodJewelry) > 0:
            price, wegiht = heap.heappop(goodJewelry)
            ans += -price
    print(ans)

