import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    n, l = map(int, input().rstrip().split())
    lis = list(map(int, input().rstrip().split()))
    que = deque()
    ans = []
    for i in range(n):
        while que and que[-1][0] > lis[i]:
            que.pop()
        while que and que[0][1] < i - l + 1:
            que.popleft()
        que.append((lis[i], i))
        print(que[0][0], end=' ')