# 자료구조, 트리를 사용한 집합과 맵, 우선순위 큐
import sys, heapq
input = sys.stdin.readline


if __name__ == '__main__':
    for _ in range(int(input().rstrip())):
        heapMax = []
        heapMin = []
        numMap = dict()
        size = 0
        for __ in range(int(input().rstrip())):
            op, val = map(str, input().rstrip().split())
            val = int(val)
            if op == 'I':
                heapq.heappush(heapMin, val)
                heapq.heappush(heapMax, -val)
                size += 1
                if val in numMap:
                    numMap[val] += 1
                else:
                    numMap[val] = 1
            elif size != 0:
                size -= 1
                if val == 1:
                    x = -heapq.heappop(heapMax)
                    numMap[x] -= 1
                else:
                    x = heapq.heappop(heapMin)
                    numMap[x] -= 1
        print(numMap)
        if size == 0:
            print("EMPTY")
        elif size == 1:
            while True:
                x = -heapq.heappop(heapMax)
                if not numMap[x] == 0:
                    print(x, x)
                    break
        else:
            maxX = 0
            minX = 0
            while True:
                x = -heapq.heappop(heapMax)
                if not numMap[x] == 0:
                    maxX = x
                    break
            while True:
                x = heapq.heappop(heapMin)
                if not numMap[x] == 0:
                    minX = x
                    break

            print(maxX, minX)