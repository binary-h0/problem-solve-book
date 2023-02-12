# 수학, 자료구조, 정수론, 우선순위 큐
input = __import__('sys').stdin.readline
heap = __import__('heapq')

if __name__ == '__main__':
    k, n = map(int, input().rstrip().split())
    ans = [0 for _ in range(100001)]
    lis = list(map(int, input().rstrip().split()))
    check = set()
    maxNum = 0
    numLis = []
    for i in lis:
        heap.heappush(numLis, i)
        if maxNum < i:
            maxNum = i
        check.add(i)

    idx = 0
    while True:
        idx += 1
        num = heap.heappop(numLis)
        if idx == n:
            print(num)
            break
        for i in range(len(lis)):
            tmp = lis[i] * num
            if not ((len(numLis) > n) and (maxNum > tmp)):
                if not tmp in check:
                    check.add(tmp)
                    heap.heappush(numLis, tmp)
                    lis.append(tmp)
                    if tmp > maxNum:
                        maxNum = tmp