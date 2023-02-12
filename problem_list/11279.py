# 자료구조, 우선순위 큐
import queue, sys
input = sys.stdin.readline


if __name__ == '__main__':
    heap = queue.PriorityQueue()
    for _ in range(int(input().rstrip())):
        x = int(input().rstrip())
        if x:
            heap.put(-x)
        else:
            if heap.empty():
                print(0)
            else:
                print(-heap.get())