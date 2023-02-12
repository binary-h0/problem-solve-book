import sys
from collections import deque
input = sys.stdin.readline

def solve(n, m, lis):
    que = deque()
    ans = 0
    for i in range(1, n + 1):
        que.append(i)
    for idx in lis:
        count = 0
        while True:
            length = len(que)
            item = que.popleft()
            if item == idx:
                ans += count if length - count > count else length - count
                break
            else:
                que.append(item)
                count += 1
    print(ans)

if __name__ == '__main__':
    N, M = map(int, input().rstrip().split())
    num_lis = list(map(int, input().rstrip().split()))
    solve(N, M, num_lis)