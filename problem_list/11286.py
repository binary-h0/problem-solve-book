# 자료구조, 우선순위 큐
import sys, queue
input = sys.stdin.readline

if __name__ == '__main__':
    heapNegative = queue.PriorityQueue()
    heapPositive = queue.PriorityQueue()

    for _ in range(int(input().rstrip())):
        x = int(input().rstrip())
        if x == 0:
            if heapNegative.empty() and heapPositive.empty():
                print(0)
            else:
                if heapNegative.empty() == heapPositive.empty():
                    n = heapNegative.get()
                    p = heapPositive.get()
                    if n <= p:
                        print(-n)
                        heapPositive.put(p)
                    else:
                        print(p)
                        heapNegative.put(n)
                else:
                    if heapNegative.empty():
                        print(heapPositive.get())
                    else:
                        print(-heapNegative.get())
        else:
            heapNegative.put(-x) if x < 0 else heapPositive.put(x)